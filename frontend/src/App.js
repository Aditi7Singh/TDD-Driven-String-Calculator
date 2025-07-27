import React, { useState } from 'react';
import './App.css';

function App() {
  const [numbers, setNumbers] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleCalculate = async () => {
    try {
      const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ numbers }),
      });
      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
        setError(null);
      } else {
        setResult(null);
        setError(data.error);
      }
    } catch (err) {
      setResult(null);
      setError('An error occurred');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>String Calculator</h1>
        <input
          type="text"
          value={numbers}
          onChange={(e) => setNumbers(e.target.value)}
          placeholder="Enter numbers"
        />
        <button onClick={handleCalculate}>Calculate</button>
        {result !== null && <h2>Result: {result}</h2>}
        {error && <h2 style={{ color: 'red' }}>Error: {error}</h2>}
      </header>
    </div>
  );
}

export default App;
