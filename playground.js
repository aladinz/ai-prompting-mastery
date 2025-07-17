document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('prompt-form');
  const input = document.getElementById('prompt-input');
  const output = document.getElementById('prompt-output');

  form.addEventListener('submit', async (e) => {
    e.preventDefault(); // ✅ Prevents page reload

    const prompt = input.value.trim();
    if (!prompt) {
      output.textContent = '⚠️ Please enter a prompt.';
      return;
    }

    output.textContent = '⏳ Thinking...';

    try {
      const res = await fetch('http://localhost:3000/api/prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });

      const data = await res.json();
      output.textContent = data.reply || '🤖 No response received.';
    } catch (err) {
      output.textContent = '❌ Error fetching response.';
      console.error(err);
    }
  });

  window.fillPrompt = function (text) {
    input.value = text;
  };
});
