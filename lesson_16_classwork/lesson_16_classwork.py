"""
Управление системой аренды недвижимости
Цель занятия:
Студенты создадут систему управления арендой недвижимости с использованием SQLAlchemy ORM.
Они будут работать с моделями, связанными через сложные отношения,
реализуют запросы с агрегациями, и применят транзакции для обработки аренды.


Система должна поддерживать следующие сущности:

Пользователь (User):
Имя (name)
Электронная почта (email)
Список договоров аренды (связь с Lease)

Объект недвижимости (Property):
Адрес (address)
Тип недвижимости (residential/commercial)
Стоимость аренды (rent_price)

Договор аренды (Lease):
Дата начала (start_date)
Дата окончания (end_date)
Арендатор (User)
Объект недвижимости (Property)
Статус (активен/завершён)

Платёж (Payment):
Сумма (amount)
Дата платежа (payment_date)
Договор аренды (Lease)


Бизнес-правила:
Один пользователь может арендовать несколько объектов недвижимости,
но не более одного договора аренды на один объект в одно и то же время. +
Договор аренды может быть активирован только после внесения первого платежа. +
Если договор завершён, объект недвижимости снова становится доступным для аренды. +
При удалении пользователя все его договоры и платежи также должны быть удалены.


ЗАДАЧА
Добавление данных:
Добавить пользователей, объекты недвижимости и договоры. +

Бизнес-логика:
Реализовать функцию для внесения платежа по договору. +
Реализовать логику завершения договора (статус "completed"). +

Сложные запросы:
Найти всех пользователей, которые не внесли ни одного платежа. +
Вывести объекты недвижимости, которые были арендованы более 3 раз. +

Транзакции:
Обеспечить атомарность операций при создании договора и внесении первого платежа. +

Расширение:
Добавить сущность "Агент" и реализовать комиссию для агентов от суммы аренды. +

Оф.документация
https://docs.sqlalchemy.org/en/20/orm/quickstart.html

"""


from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from datetime import date


# Создаём базовый класс ORM
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    leases = relationship('Lease', back_populates='user', cascade='all, delete-orphan') # каскадное удаление

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    type = Column(String, nullable=False)
    rent_price = Column(Float, nullable=False)
    leases = relationship('Lease', back_populates='property')

class Lease(Base):
    __tablename__ = 'leases'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    status = Column(Boolean, default=False)
    payments = relationship('Payment', back_populates='leases', cascade='all, delete-orphan')
    agent_id = Column(Integer, ForeignKey('agents.id'))
    agent = relationship('Agent', back_populates='leases')

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    lease_id = Column(Integer, ForeignKey('leases.id'))
    leases = relationship('Lease', back_populates='payments')



class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    commission_rate = Column(Float, nullable=False)
    leases = relationship('Lease', back_populates='agent')


engine = create_engine('sqlite:///real_estate.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_data():
    user1 = User(name='Ivan Pupkin', email='ivan.pupkin@gmail.com')
    user2 = User(name='Sergey Brui', email='sergei.brui@gmail.com')
    user3 = User(name='Anton Sklyar', email='anton.sklyar@gmail.com')
    user4 = User(name='Anna Lopatina', email='anna.lopatina@gmail.com')
    user5 = User(name='Karina Bryan', email='karina.bryan@gmail.com')

    property1 = Property(address='Minsk, Gaya 13-47', type='residential', rent_price=200)
    property2 = Property(address='Minsk, Voloha 3-152', type='residential', rent_price=180)
    property3 = Property(address='Minsk, Masherova 35-97', type='commercial', rent_price=500)
    property4 = Property(address='Brest, Pushkina 19-33', type='commercial', rent_price=150)
    property5 = Property(address='Orsha, Semenova 2-65', type='residential', rent_price=90)

    session.add_all([user1, user2, user3, user4, user5, property1, property2, property3, property4, property5])
    session.commit()

    print(f'Пользователи добавлены с ID:')
    for user in [user1, user2, user3, user4, user5]:
        print(f'Пользователь {user.name} с ID {user.id}')

    # Добавляем собственность с выводом их ID
    print(f'\nСобственность добавлена с ID:')
    for property in [property1, property2, property3, property4, property5]:
        print(f'Собственность по адресу "{property.address}" с ID {property.id}')

    lease1 = Lease(start_date=datetime.strptime('2025-01-17', '%Y-%m-%d').date(),
                   end_date=datetime.strptime('2026-01-16', '%Y-%m-%d').date(),
                   user_id=user1.id, property_id=property1.id, status=False)
    lease2 = Lease(start_date=datetime.strptime('2025-01-17', '%Y-%m-%d').date(),
                   end_date=datetime.strptime('2026-01-16', '%Y-%m-%d').date(),
                   user_id=user2.id, property_id=property2.id, status=False)
    lease3 = Lease(start_date=datetime.strptime('2025-01-30', '%Y-%m-%d').date(),
                   end_date=datetime.strptime('2026-01-30', '%Y-%m-%d').date(),
                   user_id=user3.id, property_id=property3.id, status=False)

    session.add_all([lease1, lease2, lease3])
    session.commit()

    print(f'\nДоговоры аренды добавлены с ID:')
    for lease in [lease1, lease2, lease3]:
        print(f'Договор аренды с ID {lease.id} для пользователя {lease.user_id} на собственность {lease.property_id}')

add_data()

'''
Задание - Реализовать функцию для внесения платежа по договору.
Договор аренды может быть активирован только после внесения первого платежа.
'''

def add_payment(lease_id, amount, payment_date):
    # ищем договор аренды с указанным lease_id, если он есть, добавляем платеж
    lease = session.query(Lease).filter_by(id=lease_id).first()
    if lease:
        payment = Payment(amount=amount, payment_date=payment_date, lease_id=lease_id)
        session.add(payment)
        print()
        # меняем статус договора на активный

        if not lease.status:
            lease.status = True
        session.commit()

        print(f'Платеж в размере {amount} по договору с id {lease_id} получен и договор активирован.')
    else:
        print(f'Договор аренды c id {lease_id} не найден')


'''
Задание - Реализовать логику завершения договора (статус "completed")
Если договор завершён, объект недвижимости снова становится доступным для аренды.
'''

def complete_lease(lease_id):
    lease = session.query(Lease).filter_by(id=lease_id).first()
    if lease:
        if date.today() >= lease.end_date:
            # Устанавливаем статус договора как завершённый
            lease.status = False

        # Освобождаем собственность для аренды
        lease.property.leases.clear()
        session.commit()
        print(f'Договор с id {lease_id} завершен')

    else:
        print(f'Срок действия договора с id {lease_id} еще не истек')


'''
Задание - Один пользователь может арендовать несколько объектов недвижимости,
но не более одного договора аренды на один объект в одно и то же время.

Создадим функцию, которая при создании нового договора проверяет: 
1. есть ли такой же договор у этого пользователя. 
2. есть ли активный договор на эту собственность
'''

# проверяем по пользователю и собственности
def create_lease(user_id, property_id, start_date, end_date, status=False, agent_id=None):
    overlapping_lease_user = session.query(Lease).filter(
        Lease.user_id == user_id,
        Lease.property_id == property_id,
        Lease.status == True, # только активные договоры
        Lease.start_date <= end_date, # новый договор начинается раньше окончания старого
        Lease.end_date >= start_date # новый договор заканчивается позже начала существующего
    ).first()

    if overlapping_lease_user:
        print(f'Пользователь с id {user_id} уже арендует собственность {property_id} в указанный период')
        return None

# проверяем, не занята ли собственность
    overlapping_lease_property = session.query(Lease).filter(
        Lease.property_id == property_id,
        Lease.status == True,  # только активные договоры
        Lease.start_date <= end_date,  # новый договор начинается раньше окончания старого
        Lease.end_date >= start_date  # новый договор заканчивается позже начала существующего
    ).first()

    if overlapping_lease_property:
        print(f'Нельзя создать новый договор, собственность {property_id} уже занята на указанный период')
        return None

    # если совпадений не найдено, создаем новый договор
    new_lease = Lease(
        user_id=user_id,
        property_id=property_id,
        start_date=start_date,
        end_date=end_date,
        status=status,
        agent_id=agent_id
    )
    session.add(new_lease)
    session.commit()
    print(f'Новый договор на собственность {property_id} создан успешно')
    return new_lease


add_payment(lease_id=1, amount=200, payment_date=datetime.strptime('2025-01-17', '%Y-%m-%d').date())

create_lease(user_id=1, property_id=4, start_date=datetime.strptime('2025-02-01', '%Y-%m-%d').date(),
             end_date=datetime.strptime('2025-12-31', '%Y-%m-%d').date())



'''
Сложные запросы:
Найти всех пользователей, которые не внесли ни одного платежа.
Вывести объекты недвижимости, которые были арендованы более 3 раз.
'''

# используем outerjoin, чтобы связать таблицу User с Lease и затем с Payment.
# Проверяем, где Payment.id равно None, что означает, что для этих
# договоров аренды не существует платежей

def get_users_without_payments():
    users = session.query(User).outerjoin(Lease).outerjoin(Payment).filter(Payment.id == None).all()
    return users

users_without_payments = get_users_without_payments()
for user in users_without_payments:
    print(f'Пользователь {user.name} не внёс ни одного платежа')


def get_properties():
    properties = session.query(
        Property.address,
        func.count(Lease.id).label('lease_count')
    ).join(Lease).group_by(Property.id).having(func.count(Lease.id) > 3).all()
    return properties

# Пример вызова функции
properties = get_properties()
for property_address, lease_count in properties:
    print(f'Собственность по адресу {property_address} была арендована {lease_count} раз')

'''
Транзакции:
Обеспечить атомарность операций при создании договора и внесении первого платежа.
'''

# Чтобы обеспечить атомарность операций при создании договора и внесении первого платежа,
# необходимо использовать транзакции. Это гарантирует, что обе операции
# (создание договора и внесение первого платежа) выполнятся как единое целое.
# Если произойдет ошибка в одной из операций, все изменения будут отменены.
# В SQLAlchemy транзакции можно управлять с помощью метода session.begin()
# или контекстного менеджера session.begin_nested()

def create_lease_with_first_payment(user_id, property_id, start_date, end_date, payment_amount):
    try:
        # Начало транзакции (не используем сессию с 'with session.begin()')
        # Проверяем, что нет перекрывающихся договоров на этот объект
        overlapping_lease = session.query(Lease).filter(
            Lease.property_id == property_id,
            Lease.status == True,
            Lease.start_date <= end_date,
            Lease.end_date >= start_date
        ).first()

        if overlapping_lease:
            print(f'Нельзя создать договор, объект {property_id} уже занят.')
            return None

        # Создаем новый договор аренды
        new_lease = Lease(
            user_id=user_id,
            property_id=property_id,
            start_date=start_date,
            end_date=end_date,
            status=False
        )
        session.add(new_lease)
        session.flush()  # Важно для получения ID нового объекта

        print(f"Договор аренды с ID {new_lease.id} успешно создан.")

        # Создаем первый платёж
        first_payment = Payment(
            amount=payment_amount,
            payment_date=datetime.now().date(),
            lease_id=new_lease.id  # Используем ID созданного договора
        )
        session.add(first_payment)

        # Активируем договор после первого платежа
        new_lease.status = True
        session.commit()  # Сохраняем изменения

        print(f"Первый платёж в размере {payment_amount} для договора аренды с ID {new_lease.id} успешно добавлен.")
        return new_lease

    except SQLAlchemyError as e:
        session.rollback()  # Откатываем транзакцию при ошибке
        print(f'Ошибка при создании договора и платежа: {str(e)}')
        return None





create_lease_with_first_payment(
    user_id=4,
    property_id=4,
    start_date=datetime.strptime('2025-01-20', '%Y-%m-%d').date(),
    end_date=datetime.strptime('2025-12-31', '%Y-%m-%d').date(),
    payment_amount=150
)

'''
Расширение:
Добавить сущность "Агент" и реализовать комиссию для агентов от суммы аренды.
'''

def add_agent(name, commission_rate):
    agent = Agent(name=name, commission_rate=commission_rate)
    session.add(agent)
    session.commit()
    print(f'Агент {name} успешно добавлен.')
    return agent


def calculate_agent_commission(lease_id):
    lease = session.query(Lease).filter_by(id=lease_id).first()
    if not lease or not lease.agent:
        print('Договор или агент не найден.')
        return None

    commission = lease.property.rent_price * lease.agent.commission_rate / 100
    print(f'Комиссия агента {lease.agent.name}: {commission:.2f}')
    return commission


def create_lease_with_agent(user_id, property_id, agent_id, start_date, end_date):
    try:
        # Проверка на перекрытие
        overlapping_lease = session.query(Lease).filter(
            Lease.property_id == property_id,
            Lease.status == True,
            Lease.start_date <= end_date,
            Lease.end_date >= start_date
        ).first()

        if overlapping_lease:
            print(f'Нельзя создать договор: объект {property_id} уже занят.')
            return None

        # Создаём договор аренды
        new_lease = Lease(
            user_id=user_id,
            property_id=property_id,
            agent_id=agent_id,
            start_date=start_date,
            end_date=end_date,
            status=False
        )
        session.add(new_lease)
        session.commit()
        print(f'Договор аренды с участием агента {agent_id} успешно создан.')
        return new_lease

    except Exception as e:
        session.rollback()
        print(f'Ошибка при создании договора: {str(e)}')
        return None


agent1 = add_agent(name='Mariya Agurova', commission_rate=5)

create_lease_with_agent(
    user_id=5,
    property_id=5,
    agent_id=agent1.id,
    start_date=datetime.strptime('2025-01-20', '%Y-%m-%d').date(),
    end_date=datetime.strptime('2025-12-31', '%Y-%m-%d').date()
)

calculate_agent_commission(lease_id=6)


'''
Условие:
При удалении пользователя все его договоры и платежи также должны быть удалены.

В User добавлено cascade='all, delete-orphan' для связи с Lease. 
Это означает, что если пользователь удаляется, то все его связанные аренды будут также удалены.
В Lease добавлено cascade='all, delete-orphan' для связи с Payment. 
Это гарантирует, что все платежи, связанные с арендой, будут удалены при удалении аренды.
'''

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f'Пользователь с ID {user_id} и все его данные успешно удалены.')
    else:
        print(f'Пользователь с ID {user_id} не найден.')

delete_user(3)