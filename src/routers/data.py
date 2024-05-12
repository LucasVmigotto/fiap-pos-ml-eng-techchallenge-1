from typing import Annotated
from fastapi import Depends
from pandas import DataFrame
from fastapi import APIRouter, HTTPException, Query

from utils import read_dataframe_from_code
from security.auth import get_username_from_token


router = APIRouter(
    prefix='/data',
    tags=['Data'],
    dependencies=[Depends(get_username_from_token)]
)


@router.get(
    path='/{dataframe_code}',
    description='Return the selected rows and columns of a chosen by code dataframe'
)
def get_data(dataframe_code: str,
             row_start: int = None,
             row_end: int = None,
             columns: Annotated[list[str] | None, Query()] = None,
             as_json: bool = True):
    try:
        df: DataFrame = read_dataframe_from_code(dataframe_code)

        rows_selected = range(row_start, row_end) if row_start is not None and row_end is not None else df.index

        return_df = df.loc[rows_selected, columns or df.columns]

        return return_df.to_json() if as_json else return_df.to_csv(index=False)

    except ValueError as err:
        raise HTTPException(409, str(err))

    except FileNotFoundError as err:
        raise HTTPException(404, str(err))

    except Exception as err:
        print(err)
        raise HTTPException(500, 'An unexpected error occurred')
