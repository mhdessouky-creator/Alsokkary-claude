"""
Claude Alsokkary - Main Agent Module
Intelligent AI Agent for GitHub automation and code analysis
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AlsokkaryAgent:
    """Main agent class for Claude Alsokkary"""
    
    def __init__(self, api_key: str = None):
        """Initialize the agent with Anthropic API key"""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)
        self.conversation_history = []
        self.model = "claude-3-5-sonnet-20241022"
    
    def chat(self, user_message: str) -> str:
        """Send a message to Claude and get a response"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system="You are Claude Alsokkary, an intelligent assistant specialized in GitHub automation, code analysis, and development workflows. Provide helpful, accurate, and practical advice.",
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
    
    def process_github_task(self, task: str) -> str:
        """Process GitHub-related tasks"""
        prompt = f"Process this GitHub task: {task}"
        return self.chat(prompt)


def main():
    """Main entry point"""
    print("🚀 Claude Alsokkary - Intelligent AI Agent")
    print("=" * 50)
    
    agent = AlsokkaryAgent()
    print("\n✅ Agent initialized successfully!")
    print("Type 'exit' to quit, 'reset' to clear conversation\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        
        if user_input.lower() == "reset":
            agent.reset_conversation()
            print("🔄 Conversation history cleared\n")
            continue
        
        if not user_input:
            continue
        
        print("\n🤖 Claude Alsokkary is thinking...\n")
        response = agent.chat(user_input)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()