import { useState } from "react";
const Prediction: React.FC = () => {
    const [sqft, setSqft] = useState("");
    const [bedrooms, setBedrooms] = useState("");
    const [bathrooms, setBathrooms] = useState("");
    const [condition, setCondition] = useState("");
    const [prediction, setPrediction] = useState<string | null>(null);

    const handleSubmit = async (e: React.FocusEvent<HTMLFormElement>) => {
        e.preventDefault();
        const res = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sqft, bedrooms, bathrooms, condition})
        });
        const data = await res.json();
        setPrediction(data.prediction ?? data.console.error)
    }

  return (
    <section>
        <div>
            <form onSubmit={handleSubmit}>
                <input value={sqft} onChange={(e) => setSqft(e.target.value)} placeholder="Sqft" />
                <input value={bedrooms} onChange={(e) => setBedrooms(e.target.value)} placeholder="Bedrooms" />
                <input value={bathrooms} onChange={(e) => setBathrooms(e.target.value)} placeholder="Bathrooms" />
                <input value={condition} onChange={(e) => setCondition(e.target.value)} placeholder="Condition" />
                <button type="submit">Predict</button>
                {prediction && <p>Prediction: {prediction}</p>}
            </form>
        </div>
    </section>
  )
}

export default Prediction;