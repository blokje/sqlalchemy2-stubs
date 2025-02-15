from collections import namedtuple
from typing import Any
from typing import Optional

from . import base as base
from . import coercions as coercions
from . import crud as crud
from . import elements as elements
from . import functions as functions
from . import operators as operators
from . import roles as roles
from . import schema as schema
from . import selectable as selectable
from . import sqltypes as sqltypes
from .base import NO_ARG as NO_ARG
from .base import prefix_anon_map as prefix_anon_map
from .elements import quoted_name as quoted_name
from .. import exc as exc
from .. import util as util

RESERVED_WORDS: Any
LEGAL_CHARACTERS: Any
LEGAL_CHARACTERS_PLUS_SPACE: Any
ILLEGAL_INITIAL_CHARACTERS: Any
FK_ON_DELETE: Any
FK_ON_UPDATE: Any
FK_INITIALLY: Any
BIND_PARAMS: Any
BIND_PARAMS_ESC: Any
BIND_TEMPLATES: Any
BIND_TRANSLATE: Any
OPERATORS: Any
FUNCTIONS: Any
EXTRACT_MAP: Any
COMPOUND_KEYWORDS: Any
RM_RENDERED_NAME: int
RM_NAME: int
RM_OBJECTS: int
RM_TYPE: int

ExpandedState = namedtuple(
    "ExpandedState",
    [
        "statement",
        "additional_parameters",
        "processors",
        "positiontup",
        "parameter_expansion",
    ],
)
NO_LINTING: Any
COLLECT_CARTESIAN_PRODUCTS: Any
WARN_LINTING: Any
FROM_LINTING: Any

class FromLinter:
    def lint(self, start: Optional[Any] = ...): ...
    def warn(self) -> None: ...

class Compiled:
    schema_translate_map: Any = ...
    execution_options: Any = ...
    compile_state: Any = ...
    cache_key: Any = ...
    dialect: Any = ...
    preparer: Any = ...
    statement: Any = ...
    can_execute: Any = ...
    string: Any = ...
    def __init__(
        self,
        dialect: Any,
        statement: Any,
        schema_translate_map: Optional[Any] = ...,
        render_schema_translate: bool = ...,
        compile_kwargs: Any = ...,
    ) -> None: ...
    def visit_unsupported_compilation(
        self, element: Any, err: Any
    ) -> None: ...
    @property
    def sql_compiler(self) -> None: ...
    def process(self, obj: Any, **kwargs: Any): ...
    def construct_params(
        self,
        params: Optional[Any] = ...,
        extracted_parameters: Optional[Any] = ...,
    ) -> None: ...
    @property
    def params(self): ...

class TypeCompiler:
    ensure_kwarg: str = ...
    dialect: Any = ...
    def __init__(self, dialect: Any) -> None: ...
    def process(self, type_: Any, **kw: Any): ...

class _CompileLabel(elements.ColumnElement):
    __visit_name__: str = ...
    element: Any = ...
    name: Any = ...
    def __init__(self, col: Any, name: Any, alt_names: Any = ...) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw: Any): ...

class SQLCompiler(Compiled):
    extract_map: Any = ...
    compound_keywords: Any = ...
    isdelete: bool = ...
    isinsert: bool = ...
    isupdate: bool = ...
    isplaintext: bool = ...
    returning: Any = ...
    returning_precedes_values: bool = ...
    render_table_with_column_in_update_from: bool = ...
    ansi_bind_rules: bool = ...
    insert_single_values_expr: Any = ...
    literal_execute_params: Any = ...
    post_compile_params: Any = ...
    escaped_bind_names: Any = ...
    has_out_parameters: bool = ...
    insert_prefetch: Any = ...
    update_prefetch: Any = ...
    postfetch_lastrowid: bool = ...
    inline: bool = ...
    column_keys: Any = ...
    cache_key: Any = ...
    for_executemany: Any = ...
    linting: Any = ...
    binds: Any = ...
    bind_names: Any = ...
    stack: Any = ...
    positional: Any = ...
    positiontup: Any = ...
    bindtemplate: Any = ...
    ctes: Any = ...
    label_length: Any = ...
    anon_map: Any = ...
    truncated_names: Any = ...
    def __init__(
        self,
        dialect: Any,
        statement: Any,
        cache_key: Optional[Any] = ...,
        column_keys: Optional[Any] = ...,
        for_executemany: bool = ...,
        linting: Any = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def current_executable(self): ...
    @property
    def prefetch(self): ...
    def is_subquery(self): ...
    @property
    def sql_compiler(self): ...
    def construct_params(
        self,
        params: Optional[Any] = ...,
        _group_number: Optional[Any] = ...,
        _check: bool = ...,
        extracted_parameters: Optional[Any] = ...,
    ): ...
    @property
    def params(self): ...
    def default_from(self): ...
    def visit_grouping(
        self, grouping: Any, asfrom: bool = ..., **kwargs: Any
    ): ...
    def visit_label_reference(
        self, element: Any, within_columns_clause: bool = ..., **kwargs: Any
    ): ...
    def visit_textual_label_reference(
        self, element: Any, within_columns_clause: bool = ..., **kwargs: Any
    ): ...
    def visit_label(
        self,
        label: Any,
        add_to_result_map: Optional[Any] = ...,
        within_label_clause: bool = ...,
        within_columns_clause: bool = ...,
        render_label_as_label: Optional[Any] = ...,
        result_map_targets: Any = ...,
        **kw: Any,
    ): ...
    def visit_lambda_element(self, element: Any, **kw: Any): ...
    def visit_column(
        self,
        column: Any,
        add_to_result_map: Optional[Any] = ...,
        include_table: bool = ...,
        result_map_targets: Any = ...,
        **kwargs: Any,
    ): ...
    def visit_collation(self, element: Any, **kw: Any): ...
    def visit_fromclause(self, fromclause: Any, **kwargs: Any): ...
    def visit_index(self, index: Any, **kwargs: Any): ...
    def visit_typeclause(self, typeclause: Any, **kw: Any): ...
    def post_process_text(self, text: Any): ...
    def escape_literal_column(self, text: Any): ...
    def visit_textclause(
        self,
        textclause: Any,
        add_to_result_map: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def visit_textual_select(
        self,
        taf: Any,
        compound_index: Optional[Any] = ...,
        asfrom: bool = ...,
        **kw: Any,
    ): ...
    def visit_null(self, expr: Any, **kw: Any): ...
    def visit_true(self, expr: Any, **kw: Any): ...
    def visit_false(self, expr: Any, **kw: Any): ...
    def visit_tuple(self, clauselist: Any, **kw: Any): ...
    def visit_clauselist(self, clauselist: Any, **kw: Any): ...
    def visit_case(self, clause: Any, **kwargs: Any): ...
    def visit_type_coerce(self, type_coerce: Any, **kw: Any): ...
    def visit_cast(self, cast: Any, **kwargs: Any): ...
    def visit_over(self, over: Any, **kwargs: Any): ...
    def visit_withingroup(self, withingroup: Any, **kwargs: Any): ...
    def visit_funcfilter(self, funcfilter: Any, **kwargs: Any): ...
    def visit_extract(self, extract: Any, **kwargs: Any): ...
    def visit_scalar_function_column(self, element: Any, **kw: Any): ...
    def visit_function(
        self, func: Any, add_to_result_map: Optional[Any] = ..., **kwargs: Any
    ): ...
    def visit_next_value_func(self, next_value: Any, **kw: Any): ...
    def visit_sequence(self, sequence: Any, **kw: Any) -> None: ...
    def function_argspec(self, func: Any, **kwargs: Any): ...
    compile_state: Any = ...
    def visit_compound_select(
        self,
        cs: Any,
        asfrom: bool = ...,
        compound_index: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def visit_unary(self, unary: Any, **kw: Any): ...
    def visit_is_true_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_is_false_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_empty_set_expr(self, element_types: Any) -> None: ...
    def visit_binary(
        self,
        binary: Any,
        override_operator: Optional[Any] = ...,
        eager_grouping: bool = ...,
        from_linter: Optional[Any] = ...,
        lateral_from_linter: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def visit_function_as_comparison_op_binary(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_mod_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_custom_op_binary(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_custom_op_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_custom_op_unary_modifier(
        self, element: Any, operator: Any, **kw: Any
    ): ...
    def visit_contains_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_contains_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_startswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_startswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_endswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_endswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_like_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_not_like_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_ilike_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_not_ilike_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_between_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_between_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> None: ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> None: ...
    def visit_regexp_replace_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> None: ...
    def visit_bindparam(
        self,
        bindparam: Any,
        within_columns_clause: bool = ...,
        literal_binds: bool = ...,
        skip_bind_expression: bool = ...,
        literal_execute: bool = ...,
        render_postcompile: bool = ...,
        **kwargs: Any,
    ): ...
    def render_literal_bindparam(
        self, bindparam: Any, render_literal_value: Any = ..., **kw: Any
    ): ...
    def render_literal_value(self, value: Any, type_: Any): ...
    def bindparam_string(
        self,
        name: Any,
        positional_names: Optional[Any] = ...,
        post_compile: bool = ...,
        expanding: bool = ...,
        escaped_from: Optional[Any] = ...,
        **kw: Any,
    ): ...
    execution_options: Any = ...
    ctes_recursive: bool = ...
    def visit_cte(
        self,
        cte: Any,
        asfrom: bool = ...,
        ashint: bool = ...,
        fromhints: Optional[Any] = ...,
        visiting_cte: Optional[Any] = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def visit_table_valued_alias(self, element: Any, **kw: Any): ...
    def visit_table_valued_column(self, element: Any, **kw: Any): ...
    def visit_alias(
        self,
        alias: Any,
        asfrom: bool = ...,
        ashint: bool = ...,
        iscrud: bool = ...,
        fromhints: Optional[Any] = ...,
        subquery: bool = ...,
        lateral: bool = ...,
        enclosing_alias: Optional[Any] = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def visit_subquery(self, subquery: Any, **kw: Any): ...
    def visit_lateral(self, lateral_: Any, **kw: Any): ...
    def visit_tablesample(
        self, tablesample: Any, asfrom: bool = ..., **kw: Any
    ): ...
    def visit_values(
        self,
        element: Any,
        asfrom: bool = ...,
        from_linter: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_render_as_alias_suffix(self, alias_name_text: Any): ...
    def format_from_hint_text(
        self, sqltext: Any, table: Any, hint: Any, iscrud: Any
    ): ...
    def get_select_hint_text(self, byfroms: Any) -> None: ...
    def get_from_hint_text(self, table: Any, text: Any) -> None: ...
    def get_crud_hint_text(self, table: Any, text: Any) -> None: ...
    def get_statement_hint_text(self, hint_texts: Any): ...
    translate_select_structure: Any = ...
    def visit_select(
        self,
        select_stmt: Any,
        asfrom: bool = ...,
        fromhints: Optional[Any] = ...,
        compound_index: Optional[Any] = ...,
        select_wraps_for: Optional[Any] = ...,
        lateral: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def get_cte_preamble(self, recursive: Any): ...
    def get_select_precolumns(self, select: Any, **kw: Any): ...
    def group_by_clause(self, select: Any, **kw: Any): ...
    def order_by_clause(self, select: Any, **kw: Any): ...
    def for_update_clause(self, select: Any, **kw: Any): ...
    def returning_clause(self, stmt: Any, returning_cols: Any) -> None: ...
    def limit_clause(self, select: Any, **kw: Any): ...
    def fetch_clause(self, select: Any, **kw: Any): ...
    def visit_table(
        self,
        table: Any,
        asfrom: bool = ...,
        iscrud: bool = ...,
        ashint: bool = ...,
        fromhints: Optional[Any] = ...,
        use_schema: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def visit_join(
        self,
        join: Any,
        asfrom: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def visit_insert(self, insert_stmt: Any, **kw: Any): ...
    def update_limit_clause(self, update_stmt: Any) -> None: ...
    def update_tables_clause(
        self, update_stmt: Any, from_table: Any, extra_froms: Any, **kw: Any
    ): ...
    def update_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> None: ...
    def visit_update(self, update_stmt: Any, **kw: Any): ...
    def delete_extra_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> None: ...
    def delete_table_clause(
        self, delete_stmt: Any, from_table: Any, extra_froms: Any
    ): ...
    def visit_delete(self, delete_stmt: Any, **kw: Any): ...
    def visit_savepoint(self, savepoint_stmt: Any): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt: Any): ...
    def visit_release_savepoint(self, savepoint_stmt: Any): ...

class StrSQLCompiler(SQLCompiler):
    def visit_unsupported_compilation(
        self, element: Any, err: Any, **kw: Any
    ): ...
    def visit_getitem_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_json_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_json_path_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_sequence(self, seq: Any, **kw: Any): ...
    def returning_clause(self, stmt: Any, returning_cols: Any): ...
    def update_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ): ...
    def delete_extra_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ): ...
    def visit_empty_set_expr(self, type_: Any): ...
    def get_from_hint_text(self, table: Any, text: Any): ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_regexp_replace_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...

class DDLCompiler(Compiled):
    def sql_compiler(self): ...
    def type_compiler(self): ...
    def construct_params(
        self,
        params: Optional[Any] = ...,
        extracted_parameters: Optional[Any] = ...,
    ) -> None: ...
    def visit_ddl(self, ddl: Any, **kwargs: Any): ...
    def visit_create_schema(self, create: Any, **kw: Any): ...
    def visit_drop_schema(self, drop: Any, **kw: Any): ...
    def visit_create_table(self, create: Any, **kw: Any): ...
    def visit_create_column(
        self, create: Any, first_pk: bool = ..., **kw: Any
    ): ...
    def create_table_constraints(
        self,
        table: Any,
        _include_foreign_key_constraints: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def visit_drop_table(self, drop: Any, **kw: Any): ...
    def visit_drop_view(self, drop: Any, **kw: Any): ...
    def visit_create_index(
        self,
        create: Any,
        include_schema: bool = ...,
        include_table_schema: bool = ...,
        **kw: Any,
    ): ...
    def visit_drop_index(self, drop: Any, **kw: Any): ...
    def visit_add_constraint(self, create: Any, **kw: Any): ...
    def visit_set_table_comment(self, create: Any, **kw: Any): ...
    def visit_drop_table_comment(self, drop: Any, **kw: Any): ...
    def visit_set_column_comment(self, create: Any, **kw: Any): ...
    def visit_drop_column_comment(self, drop: Any, **kw: Any): ...
    def get_identity_options(self, identity_options: Any): ...
    def visit_create_sequence(
        self, create: Any, prefix: Optional[Any] = ..., **kw: Any
    ): ...
    def visit_drop_sequence(self, drop: Any, **kw: Any): ...
    def visit_drop_constraint(self, drop: Any, **kw: Any): ...
    def get_column_specification(self, column: Any, **kwargs: Any): ...
    def create_table_suffix(self, table: Any): ...
    def post_create_table(self, table: Any): ...
    def get_column_default_string(self, column: Any): ...
    def visit_table_or_column_check_constraint(
        self, constraint: Any, **kw: Any
    ): ...
    def visit_check_constraint(self, constraint: Any, **kw: Any): ...
    def visit_column_check_constraint(self, constraint: Any, **kw: Any): ...
    def visit_primary_key_constraint(self, constraint: Any, **kw: Any): ...
    def visit_foreign_key_constraint(self, constraint: Any, **kw: Any): ...
    def define_constraint_remote_table(
        self, constraint: Any, table: Any, preparer: Any
    ): ...
    def visit_unique_constraint(self, constraint: Any, **kw: Any): ...
    def define_constraint_cascades(self, constraint: Any): ...
    def define_constraint_deferrability(self, constraint: Any): ...
    def define_constraint_match(self, constraint: Any): ...
    def visit_computed_column(self, generated: Any, **kw: Any): ...
    def visit_identity_column(self, identity: Any, **kw: Any): ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_: Any, **kw: Any): ...
    def visit_REAL(self, type_: Any, **kw: Any): ...
    def visit_NUMERIC(self, type_: Any, **kw: Any): ...
    def visit_DECIMAL(self, type_: Any, **kw: Any): ...
    def visit_INTEGER(self, type_: Any, **kw: Any): ...
    def visit_SMALLINT(self, type_: Any, **kw: Any): ...
    def visit_BIGINT(self, type_: Any, **kw: Any): ...
    def visit_TIMESTAMP(self, type_: Any, **kw: Any): ...
    def visit_DATETIME(self, type_: Any, **kw: Any): ...
    def visit_DATE(self, type_: Any, **kw: Any): ...
    def visit_TIME(self, type_: Any, **kw: Any): ...
    def visit_CLOB(self, type_: Any, **kw: Any): ...
    def visit_NCLOB(self, type_: Any, **kw: Any): ...
    def visit_CHAR(self, type_: Any, **kw: Any): ...
    def visit_NCHAR(self, type_: Any, **kw: Any): ...
    def visit_VARCHAR(self, type_: Any, **kw: Any): ...
    def visit_NVARCHAR(self, type_: Any, **kw: Any): ...
    def visit_TEXT(self, type_: Any, **kw: Any): ...
    def visit_BLOB(self, type_: Any, **kw: Any): ...
    def visit_BINARY(self, type_: Any, **kw: Any): ...
    def visit_VARBINARY(self, type_: Any, **kw: Any): ...
    def visit_BOOLEAN(self, type_: Any, **kw: Any): ...
    def visit_large_binary(self, type_: Any, **kw: Any): ...
    def visit_boolean(self, type_: Any, **kw: Any): ...
    def visit_time(self, type_: Any, **kw: Any): ...
    def visit_datetime(self, type_: Any, **kw: Any): ...
    def visit_date(self, type_: Any, **kw: Any): ...
    def visit_big_integer(self, type_: Any, **kw: Any): ...
    def visit_small_integer(self, type_: Any, **kw: Any): ...
    def visit_integer(self, type_: Any, **kw: Any): ...
    def visit_real(self, type_: Any, **kw: Any): ...
    def visit_float(self, type_: Any, **kw: Any): ...
    def visit_numeric(self, type_: Any, **kw: Any): ...
    def visit_string(self, type_: Any, **kw: Any): ...
    def visit_unicode(self, type_: Any, **kw: Any): ...
    def visit_text(self, type_: Any, **kw: Any): ...
    def visit_unicode_text(self, type_: Any, **kw: Any): ...
    def visit_enum(self, type_: Any, **kw: Any): ...
    def visit_null(self, type_: Any, **kw: Any) -> None: ...
    def visit_type_decorator(self, type_: Any, **kw: Any): ...
    def visit_user_defined(self, type_: Any, **kw: Any): ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_: Any, **kw: Any): ...
    def __getattr__(self, key: Any): ...
    def visit_null(self, type_: Any, **kw: Any): ...
    def visit_user_defined(self, type_: Any, **kw: Any): ...

class IdentifierPreparer:
    reserved_words: Any = ...
    legal_characters: Any = ...
    illegal_initial_characters: Any = ...
    schema_for_object: Any = ...
    dialect: Any = ...
    initial_quote: Any = ...
    final_quote: Any = ...
    escape_quote: Any = ...
    escape_to_quote: Any = ...
    omit_schema: Any = ...
    quote_case_sensitive_collations: Any = ...
    def __init__(
        self,
        dialect: Any,
        initial_quote: str = ...,
        final_quote: Optional[Any] = ...,
        escape_quote: str = ...,
        quote_case_sensitive_collations: bool = ...,
        omit_schema: bool = ...,
    ) -> None: ...
    def validate_sql_phrase(self, element: Any, reg: Any): ...
    def quote_identifier(self, value: Any): ...
    def quote_schema(self, schema: Any, force: Optional[Any] = ...): ...
    def quote(self, ident: Any, force: Optional[Any] = ...): ...
    def format_collation(self, collation_name: Any): ...
    def format_sequence(self, sequence: Any, use_schema: bool = ...): ...
    def format_label(self, label: Any, name: Optional[Any] = ...): ...
    def format_alias(self, alias: Any, name: Optional[Any] = ...): ...
    def format_savepoint(self, savepoint: Any, name: Optional[Any] = ...): ...
    def format_constraint(
        self, constraint: Any, _alembic_quote: bool = ...
    ): ...
    def format_index(self, index: Any): ...
    def format_table(
        self, table: Any, use_schema: bool = ..., name: Optional[Any] = ...
    ): ...
    def format_schema(self, name: Any): ...
    def format_column(
        self,
        column: Any,
        use_table: bool = ...,
        name: Optional[Any] = ...,
        table_name: Optional[Any] = ...,
        use_schema: bool = ...,
    ): ...
    def format_table_seq(self, table: Any, use_schema: bool = ...): ...
    def unformat_identifiers(self, identifiers: Any): ...
