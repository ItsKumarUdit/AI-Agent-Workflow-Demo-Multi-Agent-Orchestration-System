import React, { useState } from 'react';

function OutputPanel({ output, sessionId }) {
  const [view, setView] = useState('formatted');
  if (!output) return null;

  return (
    <div className="output-panel">
      <div className="output-panel__header">
        <h2>Final Output</h2>
        <span className="session-badge">Session: {sessionId}</span>
        <div className="view-toggle">
          <button onClick={() => setView('formatted')} className={view === 'formatted' ? 'active' : ''}>Formatted</button>
          <button onClick={() => setView('raw')} className={view === 'raw' ? 'active' : ''}>Raw JSON</button>
        </div>
      </div>
      {view === 'raw' ? (
        <pre className="output-raw">{JSON.stringify(output, null, 2)}</pre>
      ) : (
        <div className="output-formatted">
          {output.executive_summary && (
            <div className="output-section"><h3>Executive Summary</h3><p>{output.executive_summary}</p></div>
          )}
          {output.key_findings && output.key_findings.length > 0 && (
            <div className="output-section"><h3>Key Findings</h3>
              <ul>{output.key_findings.map((f, i) => <li key={i}>{f}</li>)}</ul>
            </div>
          )}
          {output.recommendations && output.recommendations.length > 0 && (
            <div className="output-section"><h3>Recommendations</h3>
              <ul>{output.recommendations.map((r, i) => <li key={i}>{r}</li>)}</ul>
            </div>
          )}
          {output.metadata && (
            <div className="output-metadata">
              <small>Generated: {output.metadata.generated_at}</small>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default OutputPanel;
