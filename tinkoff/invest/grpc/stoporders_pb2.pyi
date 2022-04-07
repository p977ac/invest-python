"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import tinkoff.invest.grpc.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _StopOrderDirection:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _StopOrderDirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopOrderDirection.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_ORDER_DIRECTION_UNSPECIFIED: _StopOrderDirection.ValueType  # 0
    """Значение не указано."""

    STOP_ORDER_DIRECTION_BUY: _StopOrderDirection.ValueType  # 1
    """Покупка."""

    STOP_ORDER_DIRECTION_SELL: _StopOrderDirection.ValueType  # 2
    """Продажа."""

class StopOrderDirection(_StopOrderDirection, metaclass=_StopOrderDirectionEnumTypeWrapper):
    """Направление сделки стоп-заявки."""
    pass

STOP_ORDER_DIRECTION_UNSPECIFIED: StopOrderDirection.ValueType  # 0
"""Значение не указано."""

STOP_ORDER_DIRECTION_BUY: StopOrderDirection.ValueType  # 1
"""Покупка."""

STOP_ORDER_DIRECTION_SELL: StopOrderDirection.ValueType  # 2
"""Продажа."""

global___StopOrderDirection = StopOrderDirection


class _StopOrderExpirationType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _StopOrderExpirationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopOrderExpirationType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED: _StopOrderExpirationType.ValueType  # 0
    """Значение не указано."""

    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL: _StopOrderExpirationType.ValueType  # 1
    """Действительно до отмены."""

    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE: _StopOrderExpirationType.ValueType  # 2
    """Действительно до даты снятия."""

class StopOrderExpirationType(_StopOrderExpirationType, metaclass=_StopOrderExpirationTypeEnumTypeWrapper):
    """Тип экспирации стоп-заявке."""
    pass

STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED: StopOrderExpirationType.ValueType  # 0
"""Значение не указано."""

STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL: StopOrderExpirationType.ValueType  # 1
"""Действительно до отмены."""

STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE: StopOrderExpirationType.ValueType  # 2
"""Действительно до даты снятия."""

global___StopOrderExpirationType = StopOrderExpirationType


class _StopOrderType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _StopOrderTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StopOrderType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STOP_ORDER_TYPE_UNSPECIFIED: _StopOrderType.ValueType  # 0
    """Значение не указано."""

    STOP_ORDER_TYPE_TAKE_PROFIT: _StopOrderType.ValueType  # 1
    """Take-profit заявка."""

    STOP_ORDER_TYPE_STOP_LOSS: _StopOrderType.ValueType  # 2
    """Stop-loss заявка."""

    STOP_ORDER_TYPE_STOP_LIMIT: _StopOrderType.ValueType  # 3
    """Stop-limit заявка."""

class StopOrderType(_StopOrderType, metaclass=_StopOrderTypeEnumTypeWrapper):
    """Тип стоп-заявки."""
    pass

STOP_ORDER_TYPE_UNSPECIFIED: StopOrderType.ValueType  # 0
"""Значение не указано."""

STOP_ORDER_TYPE_TAKE_PROFIT: StopOrderType.ValueType  # 1
"""Take-profit заявка."""

STOP_ORDER_TYPE_STOP_LOSS: StopOrderType.ValueType  # 2
"""Stop-loss заявка."""

STOP_ORDER_TYPE_STOP_LIMIT: StopOrderType.ValueType  # 3
"""Stop-limit заявка."""

global___StopOrderType = StopOrderType


class PostStopOrderRequest(google.protobuf.message.Message):
    """Запрос выставления стоп-заявки."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FIGI_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    STOP_PRICE_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    EXPIRATION_TYPE_FIELD_NUMBER: builtins.int
    STOP_ORDER_TYPE_FIELD_NUMBER: builtins.int
    EXPIRE_DATE_FIELD_NUMBER: builtins.int
    figi: typing.Text
    """Figi-идентификатор инструмента."""

    quantity: builtins.int
    """Количество лотов."""

    @property
    def price(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Цена за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""
        pass
    @property
    def stop_price(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Стоп-цена заявки за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""
        pass
    direction: global___StopOrderDirection.ValueType
    """Направление операции."""

    account_id: typing.Text
    """Номер счёта."""

    expiration_type: global___StopOrderExpirationType.ValueType
    """Тип экспирации заявки."""

    stop_order_type: global___StopOrderType.ValueType
    """Тип заявки."""

    @property
    def expire_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время окончания действия стоп-заявки в часовом поясе UTC. **Для ExpirationType = GoodTillDate заполнение обязательно**."""
        pass
    def __init__(self,
        *,
        figi: typing.Text = ...,
        quantity: builtins.int = ...,
        price: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        stop_price: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        direction: global___StopOrderDirection.ValueType = ...,
        account_id: typing.Text = ...,
        expiration_type: global___StopOrderExpirationType.ValueType = ...,
        stop_order_type: global___StopOrderType.ValueType = ...,
        expire_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expire_date",b"expire_date","price",b"price","stop_price",b"stop_price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","direction",b"direction","expiration_type",b"expiration_type","expire_date",b"expire_date","figi",b"figi","price",b"price","quantity",b"quantity","stop_order_type",b"stop_order_type","stop_price",b"stop_price"]) -> None: ...
global___PostStopOrderRequest = PostStopOrderRequest

class PostStopOrderResponse(google.protobuf.message.Message):
    """Результат выставления стоп-заявки."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STOP_ORDER_ID_FIELD_NUMBER: builtins.int
    stop_order_id: typing.Text
    """Уникальный идентификатор стоп-заявки."""

    def __init__(self,
        *,
        stop_order_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stop_order_id",b"stop_order_id"]) -> None: ...
global___PostStopOrderResponse = PostStopOrderResponse

class GetStopOrdersRequest(google.protobuf.message.Message):
    """Запрос получения списка активных стоп-заявок."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Идентификатор счёта клиента."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id"]) -> None: ...
global___GetStopOrdersRequest = GetStopOrdersRequest

class GetStopOrdersResponse(google.protobuf.message.Message):
    """Список активных стоп-заявок."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STOP_ORDERS_FIELD_NUMBER: builtins.int
    @property
    def stop_orders(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StopOrder]:
        """Массив стоп-заявок по счёту."""
        pass
    def __init__(self,
        *,
        stop_orders: typing.Optional[typing.Iterable[global___StopOrder]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stop_orders",b"stop_orders"]) -> None: ...
global___GetStopOrdersResponse = GetStopOrdersResponse

class CancelStopOrderRequest(google.protobuf.message.Message):
    """Запрос отмены выставленной стоп-заявки."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    STOP_ORDER_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Идентификатор счёта клиента."""

    stop_order_id: typing.Text
    """Уникальный идентификатор стоп-заявки."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        stop_order_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","stop_order_id",b"stop_order_id"]) -> None: ...
global___CancelStopOrderRequest = CancelStopOrderRequest

class CancelStopOrderResponse(google.protobuf.message.Message):
    """Результат отмены выставленной стоп-заявки."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIME_FIELD_NUMBER: builtins.int
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Время отмены заявки в часовом поясе UTC."""
        pass
    def __init__(self,
        *,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["time",b"time"]) -> None: ...
global___CancelStopOrderResponse = CancelStopOrderResponse

class StopOrder(google.protobuf.message.Message):
    """Информация о стоп-заявке."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STOP_ORDER_ID_FIELD_NUMBER: builtins.int
    LOTS_REQUESTED_FIELD_NUMBER: builtins.int
    FIGI_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    ORDER_TYPE_FIELD_NUMBER: builtins.int
    CREATE_DATE_FIELD_NUMBER: builtins.int
    ACTIVATION_DATE_TIME_FIELD_NUMBER: builtins.int
    EXPIRATION_TIME_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    STOP_PRICE_FIELD_NUMBER: builtins.int
    stop_order_id: typing.Text
    """Идентификатор-идентификатор стоп-заявки."""

    lots_requested: builtins.int
    """Запрошено лотов."""

    figi: typing.Text
    """Figi-идентификатор инструмента."""

    direction: global___StopOrderDirection.ValueType
    """Направление операции."""

    currency: typing.Text
    """Валюта стоп-заявки."""

    order_type: global___StopOrderType.ValueType
    """Тип стоп-заявки."""

    @property
    def create_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время выставления заявки в часовом поясе UTC."""
        pass
    @property
    def activation_date_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время конвертации стоп-заявки в биржевую в часовом поясе UTC."""
        pass
    @property
    def expiration_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время снятия заявки в часовом поясе UTC."""
        pass
    @property
    def price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Цена заявки за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""
        pass
    @property
    def stop_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Цена активации стоп-заявки за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""
        pass
    def __init__(self,
        *,
        stop_order_id: typing.Text = ...,
        lots_requested: builtins.int = ...,
        figi: typing.Text = ...,
        direction: global___StopOrderDirection.ValueType = ...,
        currency: typing.Text = ...,
        order_type: global___StopOrderType.ValueType = ...,
        create_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        activation_date_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        expiration_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        stop_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["activation_date_time",b"activation_date_time","create_date",b"create_date","expiration_time",b"expiration_time","price",b"price","stop_price",b"stop_price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activation_date_time",b"activation_date_time","create_date",b"create_date","currency",b"currency","direction",b"direction","expiration_time",b"expiration_time","figi",b"figi","lots_requested",b"lots_requested","order_type",b"order_type","price",b"price","stop_order_id",b"stop_order_id","stop_price",b"stop_price"]) -> None: ...
global___StopOrder = StopOrder
