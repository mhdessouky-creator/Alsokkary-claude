"""
Prompt Optimization Module for Claude Alsokkary
Handles prompt enhancement, refinement, and optimization
"""

from typing import List, Dict, Tuple
import json

class PromptOptimizer:
    """Optimize and enhance prompts for better Claude responses"""
    
    def __init__(self):
        self.optimization_techniques = {
            "clarity": self._enhance_clarity,
            "specificity": self._add_specificity,
            "context": self._add_context,
            "structure": self._structure_prompt,
            "examples": self._add_examples
        }
        self.prompt_templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Load prompt templates"""
        return {
            "code_review": "Review the following code for issues:\n{code}\nFocus on: {focus_areas}",
            "github_task": "Help me with this GitHub task:\n{task}\nContext: {context}",
            "optimization": "Optimize this {type}:\n{content}\nCriteria: {criteria}",
            "debugging": "Help me debug this issue:\n{issue}\nError: {error}\nSteps: {steps}"
        }
    
    def optimize(self, prompt: str, techniques: List[str] = None) -> str:
        """Apply optimization techniques to a prompt"""
        if techniques is None:
            techniques = ["clarity", "specificity", "structure"]
        
        optimized = prompt
        for technique in techniques:
            if technique in self.optimization_techniques:
                optimized = self.optimization_techniques[technique](optimized)
        
        return optimized
    
    def _enhance_clarity(self, prompt: str) -> str:
        """Enhance prompt clarity"""
        clarity_rules = {
            "replace": [
                ("please", ""),
                ("thanks", ""),
                ("okay", "")
            ],
            "add": [
                "Be concise and direct.",
                "Provide specific examples.",
                "Focus on actionable insights."
            ]
        }
        
        enhanced = prompt
        for old, new in clarity_rules["replace"]:
            enhanced = enhanced.replace(old, new)
        
        enhanced += "\n\n" + " ".join(clarity_rules["add"])
        return enhanced.strip()
    
    def _add_specificity(self, prompt: str) -> str:
        """Add specificity to prompt"""
        specificity_additions = [
            "Provide specific examples or code snippets.",
            "Include exact error messages or outputs.",
            "Specify the programming language if applicable.",
            "Mention version numbers of tools/libraries."
        ]
        
        return prompt + "\n\n" + "\n".join(f"- {item}" for item in specificity_additions)
    
    def _add_context(self, prompt: str) -> str:
        """Add context to prompt"""
        context_template = """
CONTEXT INFORMATION:
- Purpose: {purpose}
- Constraints: {constraints}
- Expected Output: {output}
        """
        return prompt + context_template
    
    def _structure_prompt(self, prompt: str) -> str:
        """Structure prompt for better response"""
        structure = f"""
TASK: {prompt}

REQUIREMENTS:
1. Provide clear, step-by-step guidance
2. Include code examples where applicable
3. Highlight important considerations
4. Suggest best practices

FORMAT:
- Use bullet points for lists
- Use code blocks for code
- Use bold for key terms
        """
        return structure.strip()
    
    def _add_examples(self, prompt: str) -> str:
        """Add examples to prompt"""
        examples_section = """
EXAMPLES:
- Good: [Specific example of what's expected]
- Avoid: [Example of what to avoid]
        """
        return prompt + "\n" + examples_section
    
    def get_optimized_prompt(self, prompt_type: str, **kwargs) -> str:
        """Get and optimize a template-based prompt"""
        if prompt_type not in self.prompt_templates:
            raise ValueError(f"Unknown prompt type: {prompt_type}")
        
        template = self.prompt_templates[prompt_type]
        prompt = template.format(**kwargs)
        
        return self.optimize(prompt)
    
    def batch_optimize(self, prompts: List[str]) -> List[str]:
        """Optimize multiple prompts at once"""
        return [self.optimize(p) for p in prompts]
    
    def analyze_prompt_quality(self, prompt: str) -> Dict[str, any]:
        """Analyze prompt quality and provide suggestions"""
        analysis = {
            "length": len(prompt.split()),
            "clarity_score": self._calculate_clarity(prompt),
            "specificity_score": self._calculate_specificity(prompt),
            "structure_score": self._calculate_structure(prompt),
            "suggestions": self._get_suggestions(prompt)
        }
        return analysis
    
    def _calculate_clarity(self, prompt: str) -> float:
        """Calculate clarity score (0-100)"""
        clarity_keywords = ["specific", "exact", "clear", "show", "provide"]
        score = sum(10 for keyword in clarity_keywords if keyword in prompt.lower())
        return min(score, 100)
    
    def _calculate_specificity(self, prompt: str) -> float:
        """Calculate specificity score (0-100)"""
        return len(prompt.split()) / 2  # Simplified calculation
    
    def _calculate_structure(self, prompt: str) -> float:
        """Calculate structure score (0-100)"""
        has_sections = prompt.count("\n") >= 2
        has_format = any(x in prompt for x in [":", "1.", "-", "*"])
        return 50 if has_sections and has_format else 25
    
    def _get_suggestions(self, prompt: str) -> List[str]:
        """Get suggestions for prompt improvement"""
        suggestions = []
        
        if len(prompt.split()) < 10:
            suggestions.append("Add more context and details")
        
        if prompt.count("\n") < 2:
            suggestions.append("Use sections or bullet points for clarity")
        
        if not any(x in prompt for x in ["example", "code", "specific"]):
            suggestions.append("Include examples or specific cases")
        
        return suggestions


def create_advanced_prompt(task: str, context: str, constraints: str, examples: List[str]) -> str:
    """Create an advanced optimized prompt"""
    optimizer = PromptOptimizer()
    
    advanced_prompt = f"""
MAIN TASK:
{task}

CONTEXT:
{context}

CONSTRAINTS:
{constraints}

EXAMPLES:
{chr(10).join(f'- {ex}' for ex in examples)}

RESPONSE GUIDELINES:
1. Be direct and concise
2. Provide step-by-step guidance
3. Include code examples where relevant
4. Highlight important considerations
5. Suggest best practices
    """
    
    return optimizer.optimize(advanced_prompt, techniques=["clarity", "specificity", "structure"])


if __name__ == "__main__":
    # Example usage
    optimizer = PromptOptimizer()
    
    sample_prompt = "Can you help me with my GitHub issue?"
    optimized = optimizer.optimize(sample_prompt)
    
    print("Original Prompt:")
    print(sample_prompt)
    print("\nOptimized Prompt:")
    print(optimized)
    
    # Analyze quality
    analysis = optimizer.analyze_prompt_quality(optimized)
    print("\nQuality Analysis:")
    print(json.dumps(analysis, indent=2))
