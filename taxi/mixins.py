from typing import Any, ClassVar

from django.views.generic.base import ContextMixin

from taxi.table_spec import TABLE_SPECS, TableKey, TableSpec


class TableSpecMixin(ContextMixin):
    table_spec_key: ClassVar[TableKey]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)

        spec = TABLE_SPECS[self.table_spec_key]
        headers = spec.headers

        ctx["table_spec"] = spec
        ctx["headers"] = headers
        ctx["column_widths"] = spec.column_widths
        ctx["rows_template"] = spec.rows_template

        aligns = spec.align_classes or ("",) * len(headers)
        ctx["header_cells"] = list(zip(headers, aligns, strict=True))
        return ctx


class TableHeightMixin(ContextMixin):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)

        ctx["items"] = ctx.get("object_list")
        page_obj = ctx.get("page_obj")
        ctx["start_index"] = page_obj.start_index() if page_obj else 0

        spec: TableSpec | None = ctx.get("table_spec")
        if spec is None:
            return ctx

        per_page = self._resolve_per_page(ctx)
        if isinstance(per_page, int):
            ctx["table_min_h_px"] = (
                spec.head_height + spec.row_height * per_page
            )
        return ctx

    def _resolve_per_page(self, ctx: dict[str, Any]) -> int | None:
        paginator = ctx.get("paginator")
        per_page = (
            getattr(paginator, "per_page", None)
            if ctx.get("is_paginated") and paginator is not None
            else getattr(self, "paginate_by", None)
        )
        return per_page if isinstance(per_page, int) else None


class BaseTableMixin(TableHeightMixin, TableSpecMixin):
    pass
