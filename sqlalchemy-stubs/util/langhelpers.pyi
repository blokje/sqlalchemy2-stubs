from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterator
from typing import List
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from . import compat

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_MP = TypeVar("_MP", bound=memoized_property[Any])
_MA = TypeVar("_MA", bound=HasMemoized.memoized_attribute[Any])
_HP = TypeVar("_HP", bound=hybridproperty)
_HM = TypeVar("_HM", bound=hybridmethod)

_LoaderType = Callable[[], _T]

def md5_hex(x: Any) -> str: ...

class safe_reraise:
    warn_only: bool = ...
    def __init__(self, warn_only: bool = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

def walk_subclasses(cls: Type[Any]) -> Iterator[Type[Any]]: ...
def string_or_unprintable(element: Any) -> str: ...
def clsname_as_plain_name(cls: Type[Any]) -> str: ...
def method_is_overridden(
    instance_or_cls: Any, against_method: Callable[..., Any]
) -> bool: ...
def decode_slice(slc: slice) -> Tuple[Any, ...]: ...
def map_bits(fn: Callable[[int], _T], n: Any) -> Iterator[_T]: ...
def decorator(target: Any) -> Any: ...
def public_factory(
    target: Any, location: Any, class_location: Optional[Any] = ...
) -> Any: ...

class PluginLoader(Generic[_T]):
    group: str = ...
    impls: Dict[str, Union[_LoaderType[_T], _T]] = ...
    auto_fn: Optional[Callable[[str], Optional[_T]]] = ...
    def __init__(
        self,
        group: str,
        auto_fn: Optional[Callable[[str], Optional[_T]]] = ...,
    ) -> None: ...
    def clear(self) -> None: ...
    def load(self, name: str) -> _T: ...
    def register(self, name: str, modulepath: str, objname: str) -> None: ...

def get_cls_kwargs(
    cls: Type[Any], _set: Optional[Set[str]] = ...
) -> Set[str]: ...
def get_func_kwargs(func: Any) -> List[str]: ...
def get_callable_argspec(
    fn: Callable[..., Any], no_self: bool = ..., _is_init: bool = ...
) -> compat.FullArgSpec: ...
def format_argspec_plus(fn: Any, grouped: bool = ...) -> Any: ...
def format_argspec_init(method: Any, grouped: bool = ...) -> Any: ...
def create_proxy_methods(
    target_cls: Any,
    target_cls_sphinx_name: Any,
    proxy_cls_sphinx_name: Any,
    classmethods: Any = ...,
    methods: Any = ...,
    attributes: Any = ...,
) -> Any: ...
def getargspec_init(
    method: Any,
) -> Union[
    compat.FullArgSpec,
    Tuple[List[str], Optional[str], Optional[str], Optional[str]],
]: ...
def unbound_method_to_callable(func_or_cls: Any) -> Any: ...
def generic_repr(
    obj: Any,
    additional_kw: Any = ...,
    to_inspect: Optional[Any] = ...,
    omit_kwarg: Any = ...,
) -> str: ...

class portable_instancemethod:
    target: Any = ...
    name: Any = ...
    kwargs: Any = ...
    def __init__(self, meth: Any, kwargs: Tuple[Any, ...] = ...) -> None: ...
    def __call__(self, *arg: Any, **kw: Any) -> Any: ...

def class_hierarchy(cls: Type[Any]) -> List[Type[Any]]: ...
def iterate_attributes(cls: Type[Any]) -> Iterator[Tuple[str, Any]]: ...
def monkeypatch_proxied_specials(
    into_cls: Any,
    from_cls: Any,
    skip: Optional[Any] = ...,
    only: Optional[Any] = ...,
    name: str = ...,
    from_instance: Optional[Any] = ...,
) -> None: ...
def methods_equivalent(meth1: Any, meth2: Any) -> bool: ...
def as_interface(
    obj: Any,
    cls: Optional[Any] = ...,
    methods: Optional[Any] = ...,
    required: Optional[Any] = ...,
) -> Any: ...

class memoized_property(Generic[_T]):
    fget: Callable[..., _T] = ...
    __doc__: Optional[str] = ...
    __name__: str = ...
    def __init__(
        self, fget: Callable[..., _T], doc: Optional[str] = ...
    ) -> None: ...
    @overload
    def __get__(self: _MP, obj: None, cls: Any) -> _MP: ...
    @overload
    def __get__(self, obj: Any, cls: Any) -> _T: ...
    @classmethod
    def reset(cls, obj: Any, name: str) -> None: ...

def memoized_instancemethod(fn: Any) -> Any: ...

class HasMemoized:
    class memoized_attribute(Generic[_T]):
        fget: Callable[..., _T] = ...
        __doc__: Optional[str] = ...
        __name__: str = ...
        def __init__(
            self, fget: Callable[..., _T], doc: Optional[str] = ...
        ) -> None: ...
        @overload
        def __get__(self: _MA, obj: None, cls: Any) -> _MA: ...
        @overload
        def __get__(self, obj: Any, cls: Any) -> _T: ...
    @classmethod
    def memoized_instancemethod(cls, fn: Any) -> Any: ...

class MemoizedSlots:
    def __getattr__(self, key: Any) -> Any: ...

def asbool(obj: Any) -> bool: ...
def bool_or_str(*text: Any) -> Callable[[Any], Any]: ...
def asint(value: Any) -> Optional[int]: ...
def coerce_kw_type(
    kw: Dict[str, Any],
    key: str,
    type_: Type[Any],
    flexi_bool: bool = ...,
    dest: Optional[Dict[str, Any]] = ...,
) -> None: ...
def constructor_key(obj: Any, cls: Type[Any]) -> Tuple[Any, ...]: ...
def constructor_copy(obj: Any, cls: Type[_T], *args: Any, **kw: Any) -> _T: ...
def counter() -> Callable[[], Iterator[int]]: ...
def duck_type_collection(
    specimen: Any, default: Optional[Type[Any]] = ...
) -> Optional[Type[Any]]: ...
def assert_arg_type(arg: _T, argtype: Type[Any], name: str) -> _T: ...
def dictlike_iteritems(dictlike: Any) -> Iterator[Tuple[Any, Any]]: ...

class classproperty(property, Generic[_T]):
    __doc__: Optional[str] = ...
    def __init__(
        self, fget: Callable[[Any], _T], *arg: Any, **kw: Any
    ) -> None: ...
    def __get__(desc: Any, self: Any, cls: Any) -> _T: ...  # type: ignore[override]

class hybridproperty:
    func: Any = ...
    clslevel: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...
    def classlevel(self: _HP, func: Any) -> _HP: ...

class hybridmethod:
    func: Any = ...
    clslevel: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> Any: ...
    def classlevel(self: _HM, func: Any) -> _HM: ...

class _symbol(int):
    def __new__(
        self,
        name: Any,
        doc: Optional[Any] = ...,
        canonical: Optional[Any] = ...,
    ): ...
    def __reduce__(self): ...

class symbol:
    symbols: Any = ...
    def __new__(  # type: ignore[misc]
        cls,
        name: Any,
        doc: Optional[Any] = ...,
        canonical: Optional[Any] = ...,
    ) -> _symbol: ...
    @classmethod
    def parse_user_argument(
        cls,
        arg: Any,
        choices: Any,
        name: Any,
        resolve_symbol_names: bool = ...,
    ) -> Optional[_symbol]: ...

def set_creation_order(instance: Any) -> None: ...
def warn_exception(
    func: Callable[..., _T], *args: Any, **kwargs: Any
) -> _T: ...
def ellipses_string(value: str, len_: int = ...): ...
def warn(msg: str) -> None: ...
def warn_limited(msg: str, args: Any) -> None: ...
def only_once(fn: _F, retry_on_exception: bool) -> _F: ...
def chop_traceback(
    tb: Any, exclude_prefix: Any = ..., exclude_suffix: Any = ...
) -> str: ...

NoneType: Type[None]

def attrsetter(attrname: str) -> Any: ...

class EnsureKWArgType(type):
    def __init__(cls, clsname: Any, bases: Any, clsdict: Any) -> None: ...

def wrap_callable(wrapper: Any, fn: Any) -> Any: ...
def quoted_token_parser(value: str) -> List[str]: ...
def add_parameter_text(params: Any, text: str) -> Callable[[_F], _F]: ...
def inject_docstring_text(doctext: str, injecttext: str, pos: int) -> str: ...
def inject_param_text(doctext: str, inject_params: Any) -> str: ...
def repr_tuple_names(names: Sequence[str]) -> str: ...
def has_compiled_ext() -> bool: ...
