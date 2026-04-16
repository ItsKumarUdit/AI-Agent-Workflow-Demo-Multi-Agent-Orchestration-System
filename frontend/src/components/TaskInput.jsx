import React, { useState } from 'react';

const EXAMPLE_TASKS = [
  'Find top 5 customers by revenue in Q1 2024 and summarize their purchase patterns',
  'Query inventory levels across all warehouses and identify low-stock items',
  'Retrieve customer profile for C001 and provide a business summary',
];

function TaskInput({ onSubmit, loading }) {
  const [task, setTask] = useState('');
  const [sessionId] = useState(() => `session-${Date.now()}`);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!task.trim() || loading) return;
    onSubmit(task.trim(), sessionId);
  };

  return (
    <div className="task-input-container">
      <h2>Submit Enterprise Task</h2>
      <form onSubmit={handleSubmit} className="task-form">
        <textarea
          className="task-textarea"
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Describe your enterprise task..."
          rows={4}
          disabled={loading}
        />
        <div className="task-examples">
          <strong>Quick examples:</strong>
          {EXAMPLE_TASKS.map((ex, i) => (
            <button key={i} type="button" className="example-btn" onClick={() => setTask(ex)} disabled={loading}>
              {ex.substring(0, 50)}...
            </button>
          ))}
        </div>
        <button type="submit" className="submit-btn" disabled={!task.trim() || loading}>
          {loading ? 'Running Pipeline...' : 'Run Agent Pipeline'}
        </button>
      </form>
      <p className="session-info">Session: <code>{sessionId}</code></p>
    </div>
  );
}

export default TaskInput;
