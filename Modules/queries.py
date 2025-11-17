# queries.py
from utils import heart_df

#---------YOUR QUERY FUNCTION GO HERE---------#
#You can define your data querying function as per your requirements here

def query(country, state, age, Gender_selection, diagnosis):
    df = heart_df.copy()

    if country:
        df = df.query("Country in @country")

    if state:
        df = df.query("State in @state")

    if Gender_selection:
        df = df.query("Gender in @Gender_selection")

    df = df.query("age >= @age[0] & age <= @age[1]")

    if diagnosis:
        df = df.query("Diagnosis in @diagnosis")

    return df


if __name__ == "__main__":
    print("This is the queries module.")