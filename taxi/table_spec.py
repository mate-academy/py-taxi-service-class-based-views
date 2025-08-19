from dataclasses import dataclass
from types import MappingProxyType
from typing import Final, Literal, Mapping

TableKey = Literal["manufacturers", "cars", "drivers"]


@dataclass(frozen=True, slots=True)
class TableSpec:
    headers: tuple[str, ...]
    column_widths: tuple[str, ...]
    rows_template: str
    row_height: int = 41
    head_height: int = 41
    align_classes: tuple[str, ...] = tuple()


_TABLE_SPECS_REGISTRY: dict[TableKey, TableSpec] = {
    "manufacturers": TableSpec(
        headers=("#", "Name", "Country"),
        column_widths=("w-[10ch]", "", ""),
        rows_template="taxi/table_rows/manufacturers.html",
        align_classes=("text-right", "", ""),
    ),
    "cars": TableSpec(
        headers=("#", "Model", "Manufacturer", "ID"),
        column_widths=("w-[10ch]", "", "", "w-[10ch]"),
        rows_template="taxi/table_rows/cars.html",
        align_classes=("text-right", "", "", "text-right"),
    ),
    "drivers": TableSpec(
        headers=("#", "Username", "Full name"),
        column_widths=("w-[10ch]", "", ""),
        rows_template="taxi/table_rows/drivers.html",
        align_classes=("text-right", "", ""),
    ),
}

TABLE_SPECS: Final[Mapping[TableKey, TableSpec]] = MappingProxyType(
    _TABLE_SPECS_REGISTRY
)


def _validate_specs() -> None:
    for key, spec in TABLE_SPECS.items():
        header_count = len(spec.headers)
        width_count = len(spec.column_widths)

        if header_count != width_count:
            raise ValueError(
                f"TableSpec '{key}': headers({header_count}) "
                f"!= column_widths({width_count})"
            )

        if spec.row_height <= 0 or spec.head_height <= 0:
            raise ValueError(f"TableSpec '{key}': heights must be positive")

        if spec.align_classes and len(spec.align_classes) != header_count:
            align_count = len(spec.align_classes)
            raise ValueError(
                f"TableSpec '{key}': align_classes({align_count}) "
                f"!= headers({header_count})"
            )


if __debug__:
    _validate_specs()

__all__ = ("TableSpec", "TABLE_SPECS", "TableKey")
