🌧️ Rainfall Comparison Dashboard (2010–2024)

This project provides an interactive Streamlit dashboard to analyze and compare rainfall data across different Indian states using IMD rainfall datasets.
It helps visualize rainfall patterns, trends, and differences between two states over the years 2010–2024.

📂 Project Structure
rainfall-analysis/
│
├── frontend.py              # Streamlit UI for visualization
├── data_processing.py       # Data cleaning, normalization, and comparison logic
├── RS_Session_267_AU_1600_A_to_D.1.csv   # Rainfall data (raw)
├── Sub_Division_IMD_2017.csv             # IMD Subdivision rainfall data
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/build_for_bharat_submission.git
cd build_for_bharat_submission

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
uvicorn app:app --reloded
streamlit run frontend.py


🧠 Features
✅ Compare annual rainfall between two Indian states.
✅ View rainfall trends between 2010 and 2024.
✅ Interactive visualizations using Matplotlib and Streamlit charts.
✅ Simple and clean UI.
✅ Built with only CSV files (no APIs needed).

🧩 Technologies Used
Python 3.10+
Streamlit for frontend
Pandas for data processing
Matplotlib for visualization

🚀 Future Improvements
Add rainfall prediction using ML models
Integrate real-time data updates
Add district-level comparison

👨‍💻 Author
Jyotishka Chattopadhyay
