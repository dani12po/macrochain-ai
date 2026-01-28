# MacroChain AI

An AI-powered crypto market analysis agent focused on global cryptocurrency markets.

## Overview

MacroChain AI is an educational and informational tool that provides comprehensive analysis of cryptocurrency markets through the lens of macroeconomic trends, market sentiment, and on-chain indicators. The system is designed to help users understand market dynamics without providing financial advice or trading signals.

## Features

- **Macroeconomic Analysis**: Analyzes global liquidity, interest rates, and risk sentiment
- **Market Sentiment Tracking**: Monitors fear/greed indicators, news tone, and market momentum
- **On-Chain Insights**: Examines blockchain activity, flows, and network metrics
- **Educational Focus**: Provides learning-oriented explanations of market phenomena
- **LLM-Agnostic**: Compatible with various language model providers
- **Modular Architecture**: Clean, extensible codebase for easy integration

## ⚠️ Important Disclaimer

**This tool is for educational and informational purposes only. It does not provide financial advice, investment recommendations, price predictions, or trading signals. Cryptocurrency markets are highly volatile and risky. Always conduct your own research and consult with qualified financial professionals before making any investment decisions.**

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dani12po/macrochain-ai.git
cd macrochain-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (optional):
```bash
# Create a .env file for API keys if needed
# No API keys are required for basic functionality
```

## Usage

### Running the API Server

Start the FastAPI server:

```bash
python -m api.app
```

The server will run on `http://localhost:8000`

### Making Analysis Requests

Send a POST request to the `/analyze` endpoint:

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the current market trends for Bitcoin?"}'
```

### Using the Core Library

```python
from core.analyzer import MacroChainAnalyzer

analyzer = MacroChainAnalyzer()
result = analyzer.analyze("Analyze Ethereum market conditions")
print(result)
```

## Architecture

```
macrochain-ai/
├── core/           # Core analysis modules
├── services/       # Response formatting and utilities
├── api/           # FastAPI web interface
├── config/        # Configuration settings
├── prompts/       # System prompts and templates
└── examples/      # Sample queries and usage examples
```

## Integration

MacroChain AI is designed to be platform-agnostic and can be integrated with:

- **Recall Network**: For decentralized AI agent deployment
- **Custom LLM Providers**: Via the prompt-based interface
- **Web Applications**: Through the REST API
- **Trading Bots**: As an analysis module (educational use only)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions and support, please open an issue on the GitHub repository.

---

**Remember**: This is an educational tool. The cryptocurrency market carries significant risks, and past performance does not indicate future results.
