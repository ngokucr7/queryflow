import duckdb
import pandas as pd

class QueryEngine:
    def __init__(self, df1: pd.DataFrame, df2: pd.DataFrame = None):
        self.con = duckdb.connect(database=':memory:')
        self.con.register('df', df1)
        if df2 is not None:
            self.con.register('df2', df2)
        self.steps = []

    def add_step(self, step_type, details):
        self.steps.append({'type': step_type, 'details': details})
        
    def get_query(self):
        # Base query
        sql = "SELECT * FROM df"
        
        # Build logic based on steps
        for step in self.steps:
            if step['type'] == 'filter':
                sql += f" WHERE {step['details']['column']} {step['details']['operator']} {step['details']['value']}"
            elif step['type'] == 'group_by':
                sql = f"SELECT {step['details']['group_col']}, SUM({step['details']['agg_col']}) as agg_val FROM ({sql}) GROUP BY {step['details']['group_col']}"
            elif step['type'] == 'append':
                sql = f"SELECT * FROM ({sql}) UNION ALL SELECT * FROM df2"
            elif step['type'] == 'merge':
                sql = f"SELECT * FROM ({sql}) as t1 JOIN df2 as t2 ON t1.{step['details']['left_col']} = t2.{step['details']['right_col']}"
        
        return sql

    def execute(self):
        query = self.get_query()
        return self.con.execute(query).df()
