// Basic React UI for the code generator
import React, { useState } from 'react';

function App() {
  const [className, setClassName] = useState('MyWidget');
  const [variableName, setVariableName] = useState('controller');
  const [generatedCode, setGeneratedCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async () => {
    setLoading(true);
    setError('');
    setGeneratedCode('');
    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ class_name: className, variable_name: variableName })
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      setGeneratedCode(data.generated_code);
    } catch (e) {
      setError(e.message || 'Failed to generate code');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', padding: 1.5rem, border: '1px solid #e2e8f0', borderRadius: 8 }}>
      <h2 style={{ textAlign: 'center', marginBottom: 1.5rem }}>Code Generator</h2>
      
      <div style={{ marginBottom: 1.5rem }}>
        <label style={{ display: 'block', marginBottom: 0.5rem, fontWeight: 500 }}>Class Name</label>
        <input
          value={className}
          onChange={e => setClassName(e.target.value)}
          placeholder="MyWidget"
          style={{ width: '100%', padding: 0.5rem, marginBottom: 1rem, boxSizing: 'border-box' }}
        />
        <label style={{ display: 'block', marginBottom: 0.5rem, fontWeight: 500 }}>Variable Name</label>
        <input
          value={variableName}
          onChange={e => setVariableName(e.target.value)}
          placeholder="controller"
          style={{ width: '100%', padding: 0.5rem, marginBottom: 1rem, boxSizing: 'border-box' }}
        />
      </div>

      <button
        onClick={handleGenerate}
        disabled={loading}
        style={{
          width: '100%', padding: 0.75rem, background: #3b82f6, color: white,
          border: none, borderRadius: 4, cursor: loading ? 'not-allowed' : 'pointer',
          fontSize: 1rem, transition: 'background 0.2s'
        }}
      >
        {loading ? 'Generating...' : 'Generate Code'}
      </button>

      {error && (
        <div style={{ background: #fecaca, color: #991b1b, padding: 0.75rem, marginTop: 1rem, borderRadius: 4, marginBottom: 1rem }}>
          {error}
        </div>
      )}

      {generatedCode && (
        <div style={{ marginTop: 1.5rem, borderTop: '1px solid #e2e8f0', paddingTop: 1rem }}>
          <h4 style={{ marginBottom: 0.75rem, color: #374151 }}>Generated Dart Code</h4>
          <pre style={{ background: #0f0f0f, color: #c9d1d9, padding: 1rem, borderRadius: 4, overflowX: 'auto', fontFamily: 'monospace', fontSize: 0.85rem }}>
            {generatedCode}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;
