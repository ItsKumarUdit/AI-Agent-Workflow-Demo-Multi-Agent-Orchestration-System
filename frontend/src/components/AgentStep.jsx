import React, { useState } from 'react';

const STATUS_ICONS = {
  pending: '⏳',
  running: '🔄',
  done: '✅',
  error: '❌',
};

const AGENT_ICONS = {
  ResearchAgent: '🔍',
  SummarizationAgent: '📝',
  FormattingAgent: '📤',
};

function AgentStep({ step, index }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className={`agent-step agent-step--${step.status}`}>
      <div className="agent-step__header" onClick={() => setExpanded(!expanded)}>
        <span className="agent-step__index">{index + 1}</span>
        <span className="agent-step__icon">{AGENT_ICONS[step.agent] || '🤖'}</span>
        <span className="agent-step__name">{step.agent}</span>
        <span className="agent-step__status">{STATUS_ICONS[step.status]} {step.status}</span>
        {step.tool_calls && step.tool_calls.length > 0 && (
          <span className="agent-step__tools">Tools: {step.tool_calls.join(', ')}</span>
        )}
        <span className="agent-step__toggle">{expanded ? '▲' : '▼'}</span>
      </div>
      {expanded && step.output && (
        <div className="agent-step__output">
          <strong>Output:</strong>
          <pre>{typeof step.output === 'object' ? JSON.stringify(step.output, null, 2) : step.output}</pre>
        </div>
      )}
    </div>
  );
}

export default AgentStep;
