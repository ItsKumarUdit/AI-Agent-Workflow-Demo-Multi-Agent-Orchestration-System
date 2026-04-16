import React from 'react';
import AgentStep from './AgentStep';

function AgentPipeline({ steps }) {
  return (
    <div className="pipeline-container">
      <h2>Agent Pipeline Execution</h2>
      <div className="pipeline-steps">
        {steps && steps.map((step, index) => (
          <AgentStep key={index} step={step} index={index} />
        ))}
      </div>
    </div>
  );
}

export default AgentPipeline;
