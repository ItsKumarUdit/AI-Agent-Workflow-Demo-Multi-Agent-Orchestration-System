import React, { useState } from 'react';
import TaskInput from './components/TaskInput';
import AgentPipeline from './components/AgentPipeline';
import OutputPanel from './components/OutputPanel';
import './styles/App.css';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleTaskSubmit = async (task, sessionId) => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiUrl}/api/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task, session_id: sessionId }),
      });
      if (!response.ok) throw new Error('Pipeline failed');
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>AI Agent Workflow Demo</h1>
        <p>Multi-Agent Orchestration System</p>
      </header>
      <main className="app-main">
        <TaskInput onSubmit={handleTaskSubmit} loading={loading} />
        {loading && (
          <div className="loading-bar">
            <div className="loading-spinner"></div>
            <span>Running agent pipeline...</span>
          </div>
        )}
        {error && <div className="error-message">Error: {error}</div>}
        {result && (
          <>
            <AgentPipeline steps={result.steps} />
            <OutputPanel output={result.final_output} sessionId={result.session_id} />
          </>
        )}
      </main>
    </div>
  );
}

export default App;
