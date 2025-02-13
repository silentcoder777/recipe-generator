import React, { useState } from "react";
import { Bars } from "react-loader-spinner";

export function WelcomePage() {
  const [recipeValue, setInputValue] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission behavior
    setLoading(true);  // Set loading to true when making the request
    
    try {

      // define payload
      const payload = {
        recipeName: recipeValue
      };

      // Make a POST request to the backend with the recipe value
      const res = await fetch("http://localhost:5000/api/endpoint", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload), // Send recipe name as part of the request body
      });

      // Parse the JSON response from the server
      const data = await res.json();
      setResponse(data.message); // Store the response to show it in the UI
    } catch (error) {
      console.error("Error:", error);
      setResponse("There was an error processing your request.");
    }finally {
      setLoading(false);  // Set loading to false when done
    }
  };

  const handleClear = () => {
    setInputValue("");  // Clear the input field
    setResponse("");     // Clear the response box
  };

  return (
    <div className="welcome-container">
      <h1 className="welcome-text">Welcome to my Recipe Generator</h1>
      <div className="input-text-message">
        <h1>
          Please provide any recipe name to know about its ingredients
        </h1>
        <div className="input-container">
          <input
            type="text"
            value={recipeValue}
            onChange={handleChange}
            placeholder="Enter something..."
            className="input-box"
          />
           <button onClick={handleSubmit} className="submit-btn">
            Get Ingredients
          </button>
          <button onClick={handleClear} className="submit-btn">
            Clear
          </button>
        </div>
      </div>

      {/* Loading bar */}
      {loading && (
        <div className="loading-container">
          <Bars color="#4CAF50" height={50} width={50} />
        </div>
      )}

      {/* Response Box */}
      {response && (
        <div className="response-box">
          <h3>AI's recommendations:</h3>
          <p>{response}</p>
        </div>
      )}

    </div>
  );
}
