# Data analysis pandas - 210611

[pandas API reference] (https://pandas.pydata.org/docs/reference/index.html)

[pandas User Guide] (https://pandas.pydata.org/docs/user_guide/index.html)

numpy : low-level  
pandas : high-level


```python
import numpy as np
import pandas as pd
```


```python
# python version check
import sys
sys.version
```




    '3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]'




```python
# numpy version
np.__version__
```




    '1.20.1'




```python
# pandas version
pd.__version__
```




    '1.2.4'



numpy datatype : array, matrix  
pandas datatype : Series, DataFrame


```python
# 읽어오는 파일에 컬럼명이 없으면 header=None을 설정한다.
# 그렇지 않으면 첫번째 줄을 컬럼명으로 인식하기 때문이다.
# header 파라미터의 default: 'infer'
data = pd.read_csv('pdsample/num.txt', header=None)
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(data)
```




    pandas.core.frame.DataFrame




```python
# 컬럼(열)
data[0]
```




    0    1
    1    6
    Name: 0, dtype: int64




```python
type(data[0])
```




    pandas.core.series.Series




```python
# index(행)
data.iloc[0]
```




    0    1
    1    2
    2    3
    3    4
    4    5
    Name: 0, dtype: int64




```python
type(data.iloc[0])
```




    pandas.core.series.Series



            ※ pandas.core.frame.DataFrame = pandas.core.series.Series + pandas.core.series.Series


```python
# .values 하면 numpy 포맷으로 변환한다.
# 내부적으로 numpy로 되어 있기 때문에 가능하다.
data.values
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10]], dtype=int64)




```python
# '__array__'가 있으면 numpy와 호환되다.
dir(data)
```




    ['T',
     '_AXIS_LEN',
     '_AXIS_ORDERS',
     '_AXIS_REVERSED',
     '_AXIS_TO_AXIS_NUMBER',
     '_HANDLED_TYPES',
     '__abs__',
     '__add__',
     '__and__',
     '__annotations__',
     '__array__',
     '__array_priority__',
     '__array_ufunc__',
     '__array_wrap__',
     '__bool__',
     '__class__',
     '__contains__',
     '__copy__',
     '__deepcopy__',
     '__delattr__',
     '__delitem__',
     '__dict__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__finalize__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattr__',
     '__getattribute__',
     '__getitem__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__iadd__',
     '__iand__',
     '__ifloordiv__',
     '__imod__',
     '__imul__',
     '__init__',
     '__init_subclass__',
     '__invert__',
     '__ior__',
     '__ipow__',
     '__isub__',
     '__iter__',
     '__itruediv__',
     '__ixor__',
     '__le__',
     '__len__',
     '__lt__',
     '__matmul__',
     '__mod__',
     '__module__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__nonzero__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rmatmul__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__setitem__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__weakref__',
     '__xor__',
     '_accessors',
     '_accum_func',
     '_add_numeric_operations',
     '_agg_by_level',
     '_agg_examples_doc',
     '_agg_summary_and_see_also_doc',
     '_aggregate',
     '_align_frame',
     '_align_series',
     '_arith_method',
     '_attrs',
     '_box_col_values',
     '_builtin_table',
     '_can_fast_transpose',
     '_check_inplace_and_allows_duplicate_labels',
     '_check_inplace_setting',
     '_check_is_chained_assignment_possible',
     '_check_label_or_level_ambiguity',
     '_check_setitem_copy',
     '_clear_item_cache',
     '_clip_with_one_bound',
     '_clip_with_scalar',
     '_cmp_method',
     '_combine_frame',
     '_consolidate',
     '_consolidate_inplace',
     '_construct_axes_dict',
     '_construct_axes_from_arguments',
     '_construct_result',
     '_constructor',
     '_constructor_expanddim',
     '_constructor_sliced',
     '_convert',
     '_count_level',
     '_cython_table',
     '_data',
     '_dir_additions',
     '_dir_deletions',
     '_dispatch_frame_op',
     '_drop_axis',
     '_drop_labels_or_levels',
     '_ensure_valid_index',
     '_find_valid_index',
     '_flags',
     '_from_arrays',
     '_get_agg_axis',
     '_get_axis',
     '_get_axis_name',
     '_get_axis_number',
     '_get_axis_resolvers',
     '_get_block_manager_axis',
     '_get_bool_data',
     '_get_cacher',
     '_get_cleaned_column_resolvers',
     '_get_column_array',
     '_get_cython_func',
     '_get_index_resolvers',
     '_get_item_cache',
     '_get_label_or_level_values',
     '_get_numeric_data',
     '_get_value',
     '_getitem_bool_array',
     '_getitem_multilevel',
     '_gotitem',
     '_hidden_attrs',
     '_indexed_same',
     '_info_axis',
     '_info_axis_name',
     '_info_axis_number',
     '_info_repr',
     '_init_mgr',
     '_inplace_method',
     '_internal_names',
     '_internal_names_set',
     '_is_builtin_func',
     '_is_cached',
     '_is_copy',
     '_is_homogeneous_type',
     '_is_label_or_level_reference',
     '_is_label_reference',
     '_is_level_reference',
     '_is_mixed_type',
     '_is_view',
     '_iset_item',
     '_item_cache',
     '_iter_column_arrays',
     '_ix',
     '_ixs',
     '_join_compat',
     '_logical_func',
     '_logical_method',
     '_maybe_cache_changed',
     '_maybe_update_cacher',
     '_metadata',
     '_mgr',
     '_min_count_stat_function',
     '_needs_reindex_multi',
     '_obj_with_exclusions',
     '_protect_consolidate',
     '_reduce',
     '_reindex_axes',
     '_reindex_columns',
     '_reindex_index',
     '_reindex_multi',
     '_reindex_with_indexers',
     '_replace_columnwise',
     '_repr_data_resource_',
     '_repr_fits_horizontal_',
     '_repr_fits_vertical_',
     '_repr_html_',
     '_repr_latex_',
     '_reset_cache',
     '_reset_cacher',
     '_sanitize_column',
     '_selected_obj',
     '_selection',
     '_selection_list',
     '_selection_name',
     '_series',
     '_set_as_cached',
     '_set_axis',
     '_set_axis_name',
     '_set_axis_nocheck',
     '_set_is_copy',
     '_set_item',
     '_set_value',
     '_setitem_array',
     '_setitem_frame',
     '_setitem_slice',
     '_slice',
     '_stat_axis',
     '_stat_axis_name',
     '_stat_axis_number',
     '_stat_function',
     '_stat_function_ddof',
     '_take_with_is_copy',
     '_to_dict_of_blocks',
     '_try_aggregate_string_function',
     '_typ',
     '_update_inplace',
     '_validate_dtype',
     '_values',
     '_where',
     'abs',
     'add',
     'add_prefix',
     'add_suffix',
     'agg',
     'aggregate',
     'align',
     'all',
     'any',
     'append',
     'apply',
     'applymap',
     'asfreq',
     'asof',
     'assign',
     'astype',
     'at',
     'at_time',
     'attrs',
     'axes',
     'backfill',
     'between_time',
     'bfill',
     'bool',
     'boxplot',
     'clip',
     'columns',
     'combine',
     'combine_first',
     'compare',
     'convert_dtypes',
     'copy',
     'corr',
     'corrwith',
     'count',
     'cov',
     'cummax',
     'cummin',
     'cumprod',
     'cumsum',
     'describe',
     'diff',
     'div',
     'divide',
     'dot',
     'drop',
     'drop_duplicates',
     'droplevel',
     'dropna',
     'dtypes',
     'duplicated',
     'empty',
     'eq',
     'equals',
     'eval',
     'ewm',
     'expanding',
     'explode',
     'ffill',
     'fillna',
     'filter',
     'first',
     'first_valid_index',
     'flags',
     'floordiv',
     'from_dict',
     'from_records',
     'ge',
     'get',
     'groupby',
     'gt',
     'head',
     'hist',
     'iat',
     'idxmax',
     'idxmin',
     'iloc',
     'index',
     'infer_objects',
     'info',
     'insert',
     'interpolate',
     'isin',
     'isna',
     'isnull',
     'items',
     'iteritems',
     'iterrows',
     'itertuples',
     'join',
     'keys',
     'kurt',
     'kurtosis',
     'last',
     'last_valid_index',
     'le',
     'loc',
     'lookup',
     'lt',
     'mad',
     'mask',
     'max',
     'mean',
     'median',
     'melt',
     'memory_usage',
     'merge',
     'min',
     'mod',
     'mode',
     'mul',
     'multiply',
     'ndim',
     'ne',
     'nlargest',
     'notna',
     'notnull',
     'nsmallest',
     'nunique',
     'pad',
     'pct_change',
     'pipe',
     'pivot',
     'pivot_table',
     'plot',
     'pop',
     'pow',
     'prod',
     'product',
     'quantile',
     'query',
     'radd',
     'rank',
     'rdiv',
     'reindex',
     'reindex_like',
     'rename',
     'rename_axis',
     'reorder_levels',
     'replace',
     'resample',
     'reset_index',
     'rfloordiv',
     'rmod',
     'rmul',
     'rolling',
     'round',
     'rpow',
     'rsub',
     'rtruediv',
     'sample',
     'select_dtypes',
     'sem',
     'set_axis',
     'set_flags',
     'set_index',
     'shape',
     'shift',
     'size',
     'skew',
     'slice_shift',
     'sort_index',
     'sort_values',
     'squeeze',
     'stack',
     'std',
     'style',
     'sub',
     'subtract',
     'sum',
     'swapaxes',
     'swaplevel',
     'tail',
     'take',
     'to_clipboard',
     'to_csv',
     'to_dict',
     'to_excel',
     'to_feather',
     'to_gbq',
     'to_hdf',
     'to_html',
     'to_json',
     'to_latex',
     'to_markdown',
     'to_numpy',
     'to_parquet',
     'to_period',
     'to_pickle',
     'to_records',
     'to_sql',
     'to_stata',
     'to_string',
     'to_timestamp',
     'to_xarray',
     'transform',
     'transpose',
     'truediv',
     'truncate',
     'tz_convert',
     'tz_localize',
     'unstack',
     'update',
     'value_counts',
     'values',
     'var',
     'where',
     'xs']



   

웹 주소에서 데이터 불러오기


```python
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 7 columns</p>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   total_bill  244 non-null    float64
     1   tip         244 non-null    float64
     2   sex         244 non-null    object 
     3   smoker      244 non-null    object 
     4   day         244 non-null    object 
     5   time        244 non-null    object 
     6   size        244 non-null    int64  
    dtypes: float64(2), int64(1), object(4)
    memory usage: 13.5+ KB
    


```python
data.head() # 앞의 5개 보여준다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.tail() # 마지막 5개 보여준다
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.sample() # random으로 1개씩 보여준다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.sample(10) # random으로 10개씩 보여준다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>160</th>
      <td>21.50</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>109</th>
      <td>14.31</td>
      <td>4.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>183</th>
      <td>23.17</td>
      <td>6.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>60</th>
      <td>20.29</td>
      <td>3.21</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>110</th>
      <td>14.00</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>84</th>
      <td>15.98</td>
      <td>2.03</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>196</th>
      <td>10.34</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>167</th>
      <td>31.71</td>
      <td>4.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>108</th>
      <td>18.24</td>
      <td>3.76</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>135</th>
      <td>8.51</td>
      <td>1.25</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.values # 데이터만 가져온다.
```




    array([[16.99, 1.01, 'Female', ..., 'Sun', 'Dinner', 2],
           [10.34, 1.66, 'Male', ..., 'Sun', 'Dinner', 3],
           [21.01, 3.5, 'Male', ..., 'Sun', 'Dinner', 3],
           ...,
           [22.67, 2.0, 'Male', ..., 'Sat', 'Dinner', 2],
           [17.82, 1.75, 'Male', ..., 'Sat', 'Dinner', 2],
           [18.78, 3.0, 'Female', ..., 'Thur', 'Dinner', 2]], dtype=object)




```python
data.index # index 정보만 가져온다.
```




    RangeIndex(start=0, stop=244, step=1)




```python
data.columns # 현재 데이터에 column명을 확인 가능
```




    Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')




```python
# pandas는 dictionary와 attribute 방식 모두 가져올 수 있다.
# dictionary 방식 이용
# data["tip"]
data["tip"][5]
```




    4.71




```python
# attribute 방식 이용
data.tip
```




    0      1.01
    1      1.66
    2      3.50
    3      3.31
    4      3.61
           ... 
    239    5.92
    240    2.00
    241    2.00
    242    1.75
    243    3.00
    Name: tip, Length: 244, dtype: float64




```python
# KeyError
# 컬럼을 fancy indexing을 이용해서 가져올 때 index를 이용해서 가져올 수 없다.
# data[[0,2]]

data[['tip','day']] # 컬럼을 fancy indexing으로가져온다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.61</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>239</th>
      <td>5.92</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>240</th>
      <td>2.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>241</th>
      <td>2.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>242</th>
      <td>1.75</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>243</th>
      <td>3.00</td>
      <td>Thur</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 2 columns</p>
</div>




```python
# TypeError 발생
# 컬럼을 slicing을 이용해서 가져올 수 없다.
# data['tip':'day'] 

data[1:3] #  row를 slicing을 이용해서 가져올 때는 index를 이용해서 가져온다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data[3]
data.iloc[3] #indexing
```




    total_bill     23.68
    tip             3.31
    sex             Male
    smoker            No
    day              Sun
    time          Dinner
    size               2
    Name: 3, dtype: object



하나의 컬럼 또는 행 가져오면 Series로 리턴한다.  
fancy indexing을 이용해서 하나의 컬럼 또는 행을 가져오면 DataFrame으로 리턴한다.


```python
type(data.iloc[3])
```




    pandas.core.series.Series




```python
type(data.tip)
```




    pandas.core.series.Series




```python
type(data[['tip']]) # 하나의 컬럼값만 가져와도 fancy indexing으로 가져오면 return값이 DataFrame임.
```




    pandas.core.frame.DataFrame




```python
type(data['tip'])
```




    pandas.core.series.Series




```python
data.iloc[0:5] # slicing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[[0,3,5]] # fancy indexing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.29</td>
      <td>4.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 3번째 행, 1번째 열에 위치한 값
data.iloc[3][1]  # list a[0][1] array a[0,1]
```




    3.31




```python
# 3번째 행, 1번째 열에 위치한 값
data.iloc[3,1]
```




    3.31




```python
# 행: 0번째 부터 3번째 미만, 열: 1번째 부터 4번째 미만까지 위치한 값을 가져온다.
data.iloc[0:3, 1:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[[0,3,5], [1,4,5]]  # fancy indexing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>day</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.71</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



iloc는 index를 이용해서 데이터를 가져오고,  
loc는 이름을 이용해서 데이터를 가져온다.


```python
# 행은 이름이 설정되어 있지 않아서 자동으로 생성된 Range index가 이름이 된다.
data.loc[0,'tip']
```




    1.01




```python
data.loc[0:5, 'tip':'time']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc[[0,3,5], ['tip','day','time']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>day</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.71</td>
      <td>Sun</td>
      <td>Dinner</td>
    </tr>
  </tbody>
</table>
</div>



#### at
이름으로 한 위치의 값만 가져온다.


```python
data.at[0,'tip'] # data.loc[0,'tip']
```




    1.01




```python
#at은 slicing을 사용할 수 없다.
data.at[0:3, 'tip']
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-72-1bae3b0d9490> in <module>
          1 #at은 slicing을 사용할 수 없다.
    ----> 2 data.at[0:3, 'tip']
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       2154             return self.obj.loc[key]
       2155 
    -> 2156         return super().__getitem__(key)
       2157 
       2158     def __setitem__(self, key, value):
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       2101 
       2102         key = self._convert_key(key)
    -> 2103         return self.obj._get_value(*key, takeable=self._takeable)
       2104 
       2105     def __setitem__(self, key, value):
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\frame.py in _get_value(self, index, col, takeable)
       3131 
       3132         try:
    -> 3133             loc = engine.get_loc(index)
       3134             return series._values[loc]
       3135         except KeyError:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    TypeError: 'slice(0, 3, None)' is an invalid key


#### iat
iat은 인덱스 번호로 한 위치의 값을 가져온다.


```python
data.iat[0,1]  # 0행 1열
```




    1.01




```python
# iat은 슬라이싱을 사용할 수 없다.
data.iat[0:3,1]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-75-0bf5a44887e6> in <module>
          1 # iat은 슬라이싱을 사용할 수 없다.
    ----> 2 data.iat[0:3,1]
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       2100                 raise ValueError("Invalid call for scalar access (getting)!")
       2101 
    -> 2102         key = self._convert_key(key)
       2103         return self.obj._get_value(*key, takeable=self._takeable)
       2104 
    

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py in _convert_key(self, key, is_setter)
       2178         for a, i in zip(self.obj.axes, key):
       2179             if not is_integer(i):
    -> 2180                 raise ValueError("iAt based indexing can only have integer indexers")
       2181         return key
       2182 
    

    ValueError: iAt based indexing can only have integer indexers



```python
#data.tip>=5
data['tip']>=5
```




    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    239     True
    240    False
    241    False
    242    False
    243    False
    Name: tip, Length: 244, dtype: bool




```python
data.loc[0]
```




    total_bill     16.99
    tip             1.01
    sex           Female
    smoker            No
    day              Sun
    time          Dinner
    size               2
    Name: 0, dtype: object




```python
type(data['tip']>=5)
```




    pandas.core.series.Series



#### boolean indexing


```python
data[data['tip']>=5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>35.26</td>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>23</th>
      <td>39.42</td>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>39</th>
      <td>31.27</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>44</th>
      <td>30.40</td>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>46</th>
      <td>22.23</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>47</th>
      <td>32.40</td>
      <td>6.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>52</th>
      <td>34.81</td>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>59</th>
      <td>48.27</td>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>73</th>
      <td>25.28</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>83</th>
      <td>32.68</td>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>85</th>
      <td>34.83</td>
      <td>5.17</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
    </tr>
    <tr>
      <th>88</th>
      <td>24.71</td>
      <td>5.85</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>116</th>
      <td>29.93</td>
      <td>5.07</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>141</th>
      <td>34.30</td>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
    </tr>
    <tr>
      <th>142</th>
      <td>41.19</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>5</td>
    </tr>
    <tr>
      <th>143</th>
      <td>27.05</td>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
    </tr>
    <tr>
      <th>155</th>
      <td>29.85</td>
      <td>5.14</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>5</td>
    </tr>
    <tr>
      <th>156</th>
      <td>48.17</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>6</td>
    </tr>
    <tr>
      <th>170</th>
      <td>50.81</td>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>172</th>
      <td>7.25</td>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>181</th>
      <td>23.33</td>
      <td>5.65</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>183</th>
      <td>23.17</td>
      <td>6.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>185</th>
      <td>20.69</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>5</td>
    </tr>
    <tr>
      <th>197</th>
      <td>43.11</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
    </tr>
    <tr>
      <th>211</th>
      <td>25.89</td>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>212</th>
      <td>48.33</td>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>214</th>
      <td>28.17</td>
      <td>6.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
x = np.array([1,2,3,4,5])
x
```




    array([1, 2, 3, 4, 5])




```python
#x[[True,False,True,True,False]]
x[x>3]
```




    array([4, 5])




```python
data['tip'][0]
```




    1.01




```python
# data[data['tip']>=5]['tip']
data[data['tip']>=5].tip
```




    11      5.00
    23      7.58
    39      5.00
    44      5.60
    46      5.00
    47      6.00
    52      5.20
    59      6.73
    73      5.00
    83      5.00
    85      5.17
    88      5.85
    116     5.07
    141     6.70
    142     5.00
    143     5.00
    155     5.14
    156     5.00
    170    10.00
    172     5.15
    181     5.65
    183     6.50
    185     5.00
    197     5.00
    211     5.16
    212     9.00
    214     6.50
    239     5.92
    Name: tip, dtype: float64




```python
type( data[data['tip']>=5] )
```




    pandas.core.frame.DataFrame




```python
# data.tip
# data['tip']
#a = data[data['tip']>=5]
#a['tip']

data[data['tip']>=5]['tip']    #data[data['tip']>=5].tip
```




    11      5.00
    23      7.58
    39      5.00
    44      5.60
    46      5.00
    47      6.00
    52      5.20
    59      6.73
    73      5.00
    83      5.00
    85      5.17
    88      5.85
    116     5.07
    141     6.70
    142     5.00
    143     5.00
    155     5.14
    156     5.00
    170    10.00
    172     5.15
    181     5.65
    183     6.50
    185     5.00
    197     5.00
    211     5.16
    212     9.00
    214     6.50
    239     5.92
    Name: tip, dtype: float64




```python
data[data['tip']>=5].loc[:,'tip':'day']  # loc
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>39</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>46</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>52</th>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>59</th>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>73</th>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>83</th>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>85</th>
      <td>5.17</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>88</th>
      <td>5.85</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>116</th>
      <td>5.07</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>143</th>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>155</th>
      <td>5.14</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>170</th>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>172</th>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>181</th>
      <td>5.65</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>183</th>
      <td>6.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>185</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>197</th>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>211</th>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>212</th>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>214</th>
      <td>6.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>239</th>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['tip']>=5].iloc[:,1:5]  # iloc
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>39</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>46</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>52</th>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>59</th>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>73</th>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>83</th>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>85</th>
      <td>5.17</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>88</th>
      <td>5.85</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>116</th>
      <td>5.07</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>143</th>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>155</th>
      <td>5.14</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>170</th>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>172</th>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>181</th>
      <td>5.65</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>183</th>
      <td>6.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>185</th>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>197</th>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>211</th>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>212</th>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>214</th>
      <td>6.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>239</th>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['tip']>=5][['tip','day']]  # fancy indexing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>5.00</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7.58</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>39</th>
      <td>5.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.60</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>46</th>
      <td>5.00</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6.00</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>52</th>
      <td>5.20</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>59</th>
      <td>6.73</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>73</th>
      <td>5.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>83</th>
      <td>5.00</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>85</th>
      <td>5.17</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>88</th>
      <td>5.85</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>116</th>
      <td>5.07</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.70</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.00</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>143</th>
      <td>5.00</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>155</th>
      <td>5.14</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5.00</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>170</th>
      <td>10.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>172</th>
      <td>5.15</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>181</th>
      <td>5.65</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>183</th>
      <td>6.50</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>185</th>
      <td>5.00</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>197</th>
      <td>5.00</td>
      <td>Thur</td>
    </tr>
    <tr>
      <th>211</th>
      <td>5.16</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>212</th>
      <td>9.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>214</th>
      <td>6.50</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>239</th>
      <td>5.92</td>
      <td>Sat</td>
    </tr>
  </tbody>
</table>
</div>



요일이 'Sun'이거나 'Sat'의 tip과 day의 값을 가져오기


```python
# a = data[(data['day']=='Sun') | (data['day']=='Sat')][['tip','day']]
a = data[(data['day']=='Sun') | (data['day']=='Sat')]
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>238</th>
      <td>35.83</td>
      <td>4.67</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>163 rows × 7 columns</p>
</div>




```python
# day컬럼에 'Sun'와 'Sat'만 저장되어 있는지 확인
a['day'].unique()
```




    array(['Sun', 'Sat'], dtype=object)




```python
a[['tip','day']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tip</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.61</td>
      <td>Sun</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>238</th>
      <td>4.67</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>239</th>
      <td>5.92</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>240</th>
      <td>2.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>241</th>
      <td>2.00</td>
      <td>Sat</td>
    </tr>
    <tr>
      <th>242</th>
      <td>1.75</td>
      <td>Sat</td>
    </tr>
  </tbody>
</table>
<p>163 rows × 2 columns</p>
</div>



#### rename


```python
data.sample()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>38.01</td>
      <td>3.0</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['tip']
data.tip
```




    0      1.01
    1      1.66
    2      3.50
    3      3.31
    4      3.61
           ... 
    239    5.92
    240    2.00
    241    2.00
    242    1.75
    243    3.00
    Name: tip, Length: 244, dtype: float64




```python
# 정상적으로 size컬럼의 값을 가져온다.
#data['size']

# 컬럼명이 size이면 요소의 개수를 가져온다.
# 컬럼명ㅇ size이면 attribute를 이용해서 size컬럼의 값을 가져올 수 없다.
data.size
```




    1708




```python
data2 = data.rename(mapper={'size':'size_'}, axis=1) # axis=0(행,raw), axis=1(열,column)
data2 = data.rename(columns={'size':'size_'})
```


```python
data2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size_</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 7 columns</p>
</div>



### category
- category는 문자(object)보다 더 많은 기능을 할 수 있다.  
- category는 문자 또는 숫자도가능하다.  
- category는 몇개로 분류할 수 있을 때 사용한다. ex)성멸(남,여)


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   total_bill  244 non-null    float64
     1   tip         244 non-null    float64
     2   sex         244 non-null    object 
     3   smoker      244 non-null    object 
     4   day         244 non-null    object 
     5   time        244 non-null    object 
     6   size        244 non-null    int64  
    dtypes: float64(2), int64(1), object(4)
    memory usage: 13.5+ KB
    


```python
type(data['sex'])
```




    pandas.core.series.Series




```python
print(data['sex'].dtype)
```

    object
    


```python
# object를 category로 데이터 타입을 변경한다.
data['sex'] = data['sex'].astype('category')
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
     #   Column      Non-Null Count  Dtype   
    ---  ------      --------------  -----   
     0   total_bill  244 non-null    float64 
     1   tip         244 non-null    float64 
     2   sex         244 non-null    category
     3   smoker      244 non-null    object  
     4   day         244 non-null    object  
     5   time        244 non-null    object  
     6   size        244 non-null    int64   
    dtypes: category(1), float64(2), int64(1), object(3)
    memory usage: 11.9+ KB
    


```python
data.sample()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>133</th>
      <td>12.26</td>
      <td>2.0</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



data에서 female만 가져오기


```python
data[data['sex']=='Female']  # data[data.sex == 'Female']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>11</th>
      <td>35.26</td>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14.83</td>
      <td>3.02</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>10.33</td>
      <td>1.67</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>226</th>
      <td>10.09</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>229</th>
      <td>22.12</td>
      <td>2.88</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>238</th>
      <td>35.83</td>
      <td>4.67</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>87 rows × 7 columns</p>
</div>




```python
# Female만 가져왔는지 unique()를 이용해서 확인 할 수 있다.
data[data['sex']=='Female']['sex'].unique()
```




    ['Female']
    Categories (1, object): ['Female']



금요일에 온 여자만 가져오기


```python
# dictionary 방식
# data[(data['sex']=='Female')&(data['day']=='Fri')]

# attribute 방식
data[(data.sex=='Female')&(data.day=='Fri')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>93</th>
      <td>16.32</td>
      <td>4.30</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>94</th>
      <td>22.75</td>
      <td>3.25</td>
      <td>Female</td>
      <td>No</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>100</th>
      <td>11.35</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>101</th>
      <td>15.38</td>
      <td>3.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>221</th>
      <td>13.42</td>
      <td>3.48</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>223</th>
      <td>15.98</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>3</td>
    </tr>
    <tr>
      <th>225</th>
      <td>16.27</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
    <tr>
      <th>226</th>
      <td>10.09</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Female만 가져왔는지 확인한다.
data[(data.sex=='Female')&(data.day=='Fri')]['sex'].unique()
```




    ['Female']
    Categories (1, object): ['Female']




```python
# Fri만 가져왔는지 확인한다.
data[(data.sex=='Female')&(data.day=='Fri')]['day'].unique()
```




    array(['Fri'], dtype=object)




[pandas API reference] (https://pandas.pydata.org/docs/reference/index.html)     

[pandas User Guide] (https://pandas.pydata.org/docs/user_guide/index.html)

### 기능 바꾸기


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.29</td>
      <td>4.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8.77</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>26.88</td>
      <td>3.12</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.04</td>
      <td>1.96</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.78</td>
      <td>3.23</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
from functools import partial
```


```python
# head 기본 5개를 10개로 변경했다.
data.head = partial(data.head, n=10)
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.29</td>
      <td>4.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8.77</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>26.88</td>
      <td>3.12</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.04</td>
      <td>1.96</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.78</td>
      <td>3.23</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 키워드 인자로 5개를 다시 볼 수 있다.
data.head(n=5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### describe  

   - describe는 기초적인 통계분석을 해준다.


```python
# describe()의 기본은 데이터가 숫자로 된 컬럼만 가져온다.
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(data.describe())
```




    pandas.core.frame.DataFrame




```python
# pandas는 numpy 기반이라서 numpy 기능을 사용할 수 있다.
data.describe().T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>244.0</td>
      <td>19.785943</td>
      <td>8.902412</td>
      <td>3.07</td>
      <td>13.3475</td>
      <td>17.795</td>
      <td>24.1275</td>
      <td>50.81</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>244.0</td>
      <td>2.998279</td>
      <td>1.383638</td>
      <td>1.00</td>
      <td>2.0000</td>
      <td>2.900</td>
      <td>3.5625</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>size</th>
      <td>244.0</td>
      <td>2.569672</td>
      <td>0.951100</td>
      <td>1.00</td>
      <td>2.0000</td>
      <td>2.000</td>
      <td>3.0000</td>
      <td>6.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# describe()은 기본적으로 숫자형 데이터만 분석해준다.
# include옵션을 사용하면 다른 분석할 데이터 타입을 지정할 수 있다.
#data.describe(include=['object'])
data.describe(include=['float64','object'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244</td>
      <td>244</td>
      <td>244</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>151</td>
      <td>87</td>
      <td>176</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 데이터 타입이 object 일때만 가져온다.
# data.describe(include=['object'])
data.describe(include=['O'])  # 대문자 알파벳 O
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244</td>
      <td>244</td>
      <td>244</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>151</td>
      <td>87</td>
      <td>176</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.number
```




    numpy.number




```python
# data.describe(include=['float64'])
data.describe(include=np.number)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 모든 타입의 데이터를 분석할 때는 include="all"로 쓴다.
data.describe(include="all")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244</td>
      <td>244</td>
      <td>244</td>
      <td>244</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>157</td>
      <td>151</td>
      <td>87</td>
      <td>176</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.569672</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.951100</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# day컬럼의  전체 요소갯수 244개
data['day'].values.size           # values: column에 해당하는 데이터값을 다 가져옴.
```




    244



value_counts()는 unique한 값과 그 객수를 알려준다.(Series만 사용한다.)


```python
# day컬럼의 요소 카테고리별  갯수
data['day'].value_counts()
```




    Sat     87
    Sun     76
    Thur    62
    Fri     19
    Name: day, dtype: int64




```python
data['sex'].value_counts()
```




    Male      157
    Female     87
    Name: sex, dtype: int64




```python
data['size'].value_counts()
```




    2    156
    3     38
    4     37
    5      5
    1      4
    6      4
    Name: size, dtype: int64




```python
data.value_counts()  # value_counts()는 Series일 때 사용해야 의미가 있다. DataFrame인 경우 의미 없음.
```




    total_bill  tip    sex     smoker  day   time    size
    13.00       2.00   Female  Yes     Thur  Lunch   2       2
    3.07        1.00   Female  Yes     Sat   Dinner  1       1
    22.23       5.00   Male    No      Sun   Dinner  2       1
    20.69       2.45   Female  No      Sat   Dinner  4       1
                5.00   Male    No      Sun   Dinner  5       1
                                                            ..
    15.53       3.00   Male    Yes     Sat   Dinner  2       1
    15.69       1.50   Male    Yes     Sun   Dinner  2       1
                3.00   Male    Yes     Sat   Dinner  3       1
    15.77       2.23   Female  No      Sat   Dinner  2       1
    50.81       10.00  Male    Yes     Sat   Dinner  3       1
    Length: 243, dtype: int64




```python
a = (data['day']=='Sun')|(data['day']=='Sat')
a.value_counts()
```




    True     163
    False     81
    Name: day, dtype: int64




```python
# 같은 컬럼에 있는 값을 가지고 검색할 때 isin()을 사용할 수 있다.
b = data['day'].isin({'Sun','Sat'})
b.value_counts()
```




    True     163
    False     81
    Name: day, dtype: int64




```python
b.unique()
```




    array([ True, False])



### where


```python
a = np.array([1,2,3,4,])
a
```




    array([1, 2, 3, 4])




```python
# where의 인자는 조건이다.
# 조건만 넣을 경우 True의 위치를 돌려준다.
np.where(a>3)
```




    (array([3], dtype=int64),)




```python
# where는 인자 갯수에 따라서 기능이 달라진다.
# 조건이 True이면 0, False이면 100을 반환한다.
np.where(a>3, 0, 100)                           # where(조건, 조건이 참일때 리턴값, 조건이 거짓일때 리턴값)
```




    array([100, 100, 100,   0])



describe 결과를 pandas에서 제공하는 함수


```python
data['tip'].count()
```




    244




```python
data['tip'].mean()
```




    2.9982786885245902




```python
data['tip'].max()
```




    10.0




```python
data['tip'].min()
```




    1.0




```python
data['tip'].std()
```




    1.3836381890011826



describe 결과를 numpy에서 제공하는 함수


```python
import numpy.ma as ma
```


```python
kk = data.values[:,1].copy()
kk
```




    array([1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71,
           5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75,
           2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45,
           3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0,
           5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5,
           1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01,
           2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0,
           3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0,
           4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08,
           1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07,
           1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0,
           2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5,
           6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74,
           2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0,
           3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0,
           2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0,
           1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01,
           2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5,
           6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5,
           2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17,
           4.67, 5.92, 2.0, 2.0, 1.75, 3.0], dtype=object)




```python
# tips 데이터셋에서 tip만 가져옴.
xx = ma.array(data.values[:,0].copy())
```


```python
xx
```




    masked_array(data=[16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88,
                       15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58,
                       10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42,
                       19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35,
                       15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27,
                       16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4,
                       28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49,
                       38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29,
                       17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07,
                       26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29,
                       19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28,
                       24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17,
                       27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42,
                       20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25,
                       38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08,
                       11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52,
                       11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51,
                       10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05,
                       16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13,
                       17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49,
                       21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71,
                       10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9,
                       17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17,
                       40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81,
                       28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51,
                       18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73,
                       24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9,
                       28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98,
                       13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69,
                       11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03,
                       27.18, 22.67, 17.82, 18.78],
                 mask=False,
           fill_value='?',
                dtype=object)




```python
ma.count(xx)
```




    244




```python
ma.mean(xx)
```




    19.785942622950824




```python
ma.std(xx)  # 표준편차
```




    8.88415057777113




```python
kk.max()
```




    10.0




```python
kk.min()
```




    1.0




```python

```


```python

```
