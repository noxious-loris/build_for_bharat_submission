# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import qa_engine
import pandas as pd

rainfall_df = pd.read_csv("Sub_Division_IMD_2017.csv")
crop_df = pd.read_csv("RS_Session_267_AU_1600_A_to_D.1.csv")



app = FastAPI()

class NLQuery(BaseModel):
    question: str

@app.post("/ask")
def ask(q: NLQuery):
    qtext = q.question.lower()

    if "compare" in qtext and "rainfall" in qtext:
        # Simple keyword extraction
        known_states = ["Bihar", "West Bengal", "Tamil Nadu", "Maharashtra", "Karnataka", "Kerala"]
        words = qtext.split()
        states = [w.capitalize() for w in words if w.capitalize() in known_states]

        if len(states) < 2:
            return {"error": "Please mention two states to compare."}

        years = (2010, 2024)
        m = 3

        avg1, avg2, s1_df, s2_df = qa_engine.compare_states_rainfall(states[0], states[1], years)
        return {
    "answer": f"Average annual rainfall ({years[0]}–{years[1]}) — {states[0]}: {avg1:.1f} mm; {states[1]}: {avg2:.1f} mm",
    "data_preview": {
        states[0]: s1_df.head(3).to_dict(orient='records'),
        states[1]: s2_df.head(3).to_dict(orient='records')
    }
}


        top_x = qa_engine.top_crops_by_state(states[0], years, top_m=m)
        top_y = qa_engine.top_crops_by_state(states[1], years, top_m=m)

        return {
            "answer": f"Avg annual rainfall ({years[0]}–{years[1]}) — {states[0]}: {ax:.1f} mm; {states[1]}: {ay:.1f} mm",
            "top_crops": {
                states[0]: top_x.to_dict(orient='records'),
                states[1]: top_y.to_dict(orient='records')
            }
        }

    return {"answer": "I couldn’t parse the question. Try: 'Compare rainfall between Kerala and Karnataka from 2010 to 2024'."}
