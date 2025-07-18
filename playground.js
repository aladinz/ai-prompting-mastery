document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('prompt-form');
  const input = document.getElementById('prompt-input');
  const output = document.getElementById('prompt-output');

  // Mock AI responses for demonstration
  const mockResponses = {
    'write a poem about the ocean': `🌊 Ocean's Song 🌊

Deep blue waters, endless and wide,
Where mysteries and treasures hide.
Waves that dance with moonlit grace,
Time eternal in this watery space.

Currents whisper ancient tales,
Of ships with billowing sails.
The ocean breathes, alive and free,
A symphony of sea and sky to see.`,

    'summarize this article': `📰 Summary Guide 📰

To create a good summary:
1. Identify the main points
2. Keep it concise (1-3 paragraphs)
3. Use your own words
4. Include key facts and conclusions
5. Maintain the original meaning

Please paste the article text you'd like me to summarize!`,

    'explain quantum computing to a 5-year-old': `🧠 Quantum Computing for Kids 🧠

Imagine you have a magical coin that can be both heads AND tails at the same time! 

Regular computers use bits that are like normal coins - they can only be heads (1) or tails (0). But quantum computers use special "quantum bits" or "qubits" that are like magical coins.

These magical coins can try all possible answers to a problem at once, making quantum computers super fast at solving certain puzzles - like finding your way through a huge maze or cracking secret codes!

It's like having a super-smart friend who can think about many things at the same time! 🤯✨`
  };

  function generateMockResponse(prompt) {
    const lowerPrompt = prompt.toLowerCase().trim();
    
    // Check for exact template matches
    for (const [template, response] of Object.entries(mockResponses)) {
      if (lowerPrompt.includes(template.toLowerCase())) {
        return response;
      }
    }
    
    // Check for common prompt types and generate appropriate responses
    if (lowerPrompt.includes('write') || lowerPrompt.includes('create')) {
      return `✍️ Creative Response ✍️

I'd be happy to help you write something! Here's a response based on your prompt:

"${prompt}"

This is a demonstration of how AI might respond to your creative prompt. In a real AI system, you would get a detailed, contextual response tailored specifically to your request.

💡 Tip: Try being more specific about style, length, or format for better results!`;
    }
    
    if (lowerPrompt.includes('explain') || lowerPrompt.includes('what is') || lowerPrompt.includes('how does')) {
      return `🧠 Explanation 🧠

Based on your question: "${prompt}"

This is where an AI would provide a clear, educational explanation. The response would be:
- Broken down into simple concepts
- Include relevant examples
- Structured for easy understanding
- Tailored to your knowledge level

💡 Tip: Ask follow-up questions to dive deeper into specific aspects!`;
    }
    
    if (lowerPrompt.includes('summarize') || lowerPrompt.includes('summary')) {
      return `📋 Summary Response 📋

For your prompt: "${prompt}"

A real AI would analyze the provided text and create a concise summary highlighting:
- Main themes and key points
- Important facts and figures
- Core conclusions or takeaways
- Essential context

Please provide the text you'd like summarized for a more specific response!`;
    }
    
    if (lowerPrompt.includes('code') || lowerPrompt.includes('program') || lowerPrompt.includes('function')) {
      return `💻 Code Response 💻

For your coding request: "${prompt}"

Here's how an AI might help:

\`\`\`javascript
// Example: Basic function structure
function exampleFunction() {
    // AI would generate specific code based on your request
    console.log("This is a demonstration response");
    return "AI-generated code would appear here";
}
\`\`\`

💡 Tip: Be specific about programming language, requirements, and use case for better code generation!`;
    }
    
    // Default response for other prompts
    return `🤖 AI Response 🤖

Thank you for your prompt: "${prompt}"

This is a demonstration of how an AI system would respond to your input. In a real AI application, you would receive:

- A thoughtful, contextual response
- Information tailored to your specific request
- Helpful suggestions and follow-up ideas
- Accurate and relevant content

💡 Try the template buttons above for example prompts, or experiment with different types of requests!

🔧 This is a local demo - no actual AI API is being called.`;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevents page reload

    const prompt = input.value.trim();
    if (!prompt) {
      output.textContent = '⚠️ Please enter a prompt.';
      return;
    }

    output.textContent = '⏳ Thinking...';

    // Simulate AI processing delay
    setTimeout(() => {
      const response = generateMockResponse(prompt);
      output.textContent = response;
    }, 1000 + Math.random() * 1500); // Random delay between 1-2.5 seconds
  });

  window.fillPrompt = function (text) {
    input.value = text;
  };
});
