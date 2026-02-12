import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  // State management for form inputs, API responses, and UI feedback
  const [formData, setFormData] = useState({ name: "", feeling: "" });
  const [affirmation, setAffirmation] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setAffirmation("");

    try {
      // Logic: Send user input to the FastAPI backend
      const response = await axios.post(
        "https://live-mood-architect-backend.onrender.com/api/affirmation",
        formData,
      );
      
      // Update state with the AI-generated response
      setAffirmation(response.data.affirmation);
    } catch (err) {
      // User-friendly error handling without raw stack traces
      setError(
        "The AI Architect is taking a breather. Please check your connection and try again!",
      );
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>Live Mood Architect</h1>
        <p>Receive a personalized affirmation tailored to your current headspace.</p>
      </header>

      {/* Clean, responsive form interface */}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Your Name"
          required
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        />
        <textarea
          placeholder="How are you feeling today?"
          required
          value={formData.feeling}
          onChange={(e) =>
            setFormData({ ...formData, feeling: e.target.value })
          }
        />
        {/* Loading state handling to prevent duplicate submissions */}
        <button type="submit" disabled={loading}>
          {loading ? "Crafting Affirmation..." : "Generate Affirmation"}
        </button>
      </form>

      {/* Conditional rendering for Error and Results areas */}
      {error && <div className="error-box">{error}</div>}

      {affirmation && (
        <div className="result-area">
          <h3>Your Personal Affirmation</h3>
          <p>"{affirmation}"</p>
        </div>
      )}
    </div>
  );
}

export default App;