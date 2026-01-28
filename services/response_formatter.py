"""
Response formatter for MacroChain AI.

This module handles the formatting of analysis results into clean,
human-readable responses while maintaining educational focus
and neutral tone.
"""

from typing import Dict, Any, List
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


class ResponseFormatter:
    """
    Formats analysis results into user-friendly responses.
    
    This class takes structured analysis data and formats it into
    clear, educational responses that maintain neutrality and
    include appropriate disclaimers.
    """
    
    def __init__(self):
        """Initialize the response formatter."""
        self.response_sections = [
            "summary",
            "market_conditions",
            "key_insights",
            "risk_factors",
            "educational_context",
            "disclaimer"
        ]
    
    def format_analysis_response(
        self, 
        analysis_data: Dict[str, Any],
        user_query: str
    ) -> Dict[str, Any]:
        """
        Format complete analysis response.
        
        Args:
            analysis_data: Raw analysis data from core modules
            user_query: Original user query
            
        Returns:
            Formatted response dictionary
        """
        try:
            logger.info("Formatting analysis response")
            
            formatted_response = {
                "query": user_query,
                "timestamp": self._get_timestamp(),
                "summary": self._format_summary(analysis_data),
                "market_conditions": self._format_market_conditions(analysis_data),
                "analysis_sections": self._format_analysis_sections(analysis_data),
                "key_insights": self._format_key_insights(analysis_data),
                "risk_factors": self._format_risk_factors(analysis_data),
                "educational_context": self._format_educational_context(analysis_data),
                "disclaimer": self._get_standard_disclaimer(),
                "metadata": self._format_metadata(analysis_data)
            }
            
            logger.info("Response formatting completed")
            return formatted_response
            
        except Exception as e:
            logger.error(f"Error formatting response: {str(e)}")
            return self._error_response(user_query, str(e))
    
    def _format_summary(self, analysis_data: Dict[str, Any]) -> str:
        """
        Format executive summary of the analysis.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            Formatted summary string
        """
        try:
            # Extract key information
            assets = analysis_data.get("assets_analyzed", ["bitcoin", "ethereum"])
            market_conditions = analysis_data.get("market_conditions", {})
            overall_state = market_conditions.get("overall_state", "neutral")
            
            # Build summary
            summary_parts = [
                f"Analysis of {', '.join(assets).title()} market conditions.",
                f"Current market state appears {overall_state}."
            ]
            
            # Add key factors if available
            key_factors = market_conditions.get("key_factors", [])
            if key_factors:
                summary_parts.append("Key influencing factors include:")
                for factor in key_factors[:3]:  # Limit to top 3
                    summary_parts.append(f"• {factor}")
            
            # Add educational context
            summary_parts.extend([
                "",
                "This analysis examines market dynamics through multiple lenses:",
                "macroeconomic conditions, market sentiment, and on-chain indicators.",
                "The goal is to provide educational insights into market structure",
                "and dynamics, not to predict future price movements."
            ])
            
            return "\n".join(summary_parts)
            
        except Exception as e:
            logger.error(f"Error formatting summary: {str(e)}")
            return "Summary unavailable due to formatting error."
    
    def _format_market_conditions(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format market conditions section.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            Formatted market conditions
        """
        try:
            market_conditions = analysis_data.get("market_conditions", {})
            
            formatted_conditions = {
                "overall_state": market_conditions.get("overall_state", "neutral"),
                "confidence_level": market_conditions.get("confidence_level", "moderate"),
                "key_factors": market_conditions.get("key_factors", []),
                "explanation": self._get_market_state_explanation(
                    market_conditions.get("overall_state", "neutral")
                )
            }
            
            return formatted_conditions
            
        except Exception as e:
            logger.error(f"Error formatting market conditions: {str(e)}")
            return {"error": "Market conditions formatting failed"}
    
    def _format_analysis_sections(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format individual analysis sections.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            Formatted analysis sections
        """
        try:
            sections = {}
            
            # Macro analysis section
            if "macro_analysis" in analysis_data:
                sections["macroeconomic"] = self._format_macro_section(
                    analysis_data["macro_analysis"]
                )
            
            # Sentiment analysis section
            if "sentiment_analysis" in analysis_data:
                sections["sentiment"] = self._format_sentiment_section(
                    analysis_data["sentiment_analysis"]
                )
            
            # On-chain analysis section
            if "onchain_analysis" in analysis_data:
                sections["onchain"] = self._format_onchain_section(
                    analysis_data["onchain_analysis"]
                )
            
            return sections
            
        except Exception as e:
            logger.error(f"Error formatting analysis sections: {str(e)}")
            return {"error": "Analysis sections formatting failed"}
    
    def _format_macro_section(self, macro_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format macroeconomic analysis section."""
        try:
            return {
                "title": "Macroeconomic Analysis",
                "overall_conditions": macro_data.get("overall_conditions", {}),
                "key_insights": macro_data.get("insights", [])[:3],  # Top 3 insights
                "educational_notes": macro_data.get("educational_notes", [])[:2],
                "explanation": (
                    "Macroeconomic factors provide the broader context in which "
                    "cryptocurrency markets operate. These include global liquidity, "
                    "interest rate environments, and overall risk sentiment."
                )
            }
        except Exception as e:
            logger.error(f"Error formatting macro section: {str(e)}")
            return {"error": "Macro section formatting failed"}
    
    def _format_sentiment_section(self, sentiment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format sentiment analysis section."""
        try:
            return {
                "title": "Market Sentiment Analysis",
                "overall_sentiment": sentiment_data.get("overall_sentiment", {}),
                "key_insights": sentiment_data.get("insights", [])[:3],
                "educational_context": sentiment_data.get("educational_context", [])[:2],
                "explanation": (
                    "Market sentiment reflects the collective psychology of market "
                    "participants. Understanding sentiment helps explain short-term "
                    "price movements and market dynamics."
                )
            }
        except Exception as e:
            logger.error(f"Error formatting sentiment section: {str(e)}")
            return {"error": "Sentiment section formatting failed"}
    
    def _format_onchain_section(self, onchain_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format on-chain analysis section."""
        try:
            return {
                "title": "On-Chain Analysis",
                "network_conditions": onchain_data.get("network_conditions", {}),
                "key_insights": onchain_data.get("insights", [])[:3],
                "educational_explanations": onchain_data.get("educational_explanations", [])[:2],
                "explanation": (
                    "On-chain metrics provide transparent insights into network "
                    "activity and fundamentals. These indicators help assess the "
                    "actual usage and health of blockchain networks."
                )
            }
        except Exception as e:
            logger.error(f"Error formatting on-chain section: {str(e)}")
            return {"error": "On-chain section formatting failed"}
    
    def _format_key_insights(self, analysis_data: Dict[str, Any]) -> List[str]:
        """
        Format key insights from all analysis sections.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            List of formatted key insights
        """
        try:
            all_insights = []
            
            # Collect insights from different sections
            if "macro_analysis" in analysis_data:
                all_insights.extend(analysis_data["macro_analysis"].get("insights", []))
            
            if "sentiment_analysis" in analysis_data:
                all_insights.extend(analysis_data["sentiment_analysis"].get("insights", []))
            
            if "onchain_analysis" in analysis_data:
                all_insights.extend(analysis_data["onchain_analysis"].get("insights", []))
            
            # Add themes if available
            if "key_themes" in analysis_data:
                for theme in analysis_data["key_themes"]:
                    all_insights.append(f"Theme: {theme}")
            
            # Format and limit insights
            formatted_insights = []
            for insight in all_insights[:5]:  # Limit to top 5
                formatted_insights.append(f"• {insight}")
            
            return formatted_insights
            
        except Exception as e:
            logger.error(f"Error formatting key insights: {str(e)}")
            return ["• Key insights unavailable due to formatting error"]
    
    def _format_risk_factors(self, analysis_data: Dict[str, Any]) -> List[str]:
        """
        Format risk factors section.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            List of formatted risk factors
        """
        try:
            risks = analysis_data.get("risk_factors", [])
            
            # Add standard risks if none provided
            if not risks:
                risks = [
                    "Cryptocurrency market volatility",
                    "Regulatory uncertainty",
                    "Technology and security risks",
                    "Liquidity risks"
                ]
            
            # Format risks
            formatted_risks = []
            for risk in risks[:5]:  # Limit to top 5
                formatted_risks.append(f"• {risk}")
            
            return formatted_risks
            
        except Exception as e:
            logger.error(f"Error formatting risk factors: {str(e)}")
            return ["• Risk factors unavailable due to formatting error"]
    
    def _format_educational_context(self, analysis_data: Dict[str, Any]) -> str:
        """
        Format educational context section.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            Formatted educational context string
        """
        try:
            context_parts = [
                "Educational Context:",
                "",
                "This analysis demonstrates how different factors interact in cryptocurrency markets:",
                "",
                "1. **Macroeconomic factors** provide the broader market environment",
                "2. **Market sentiment** reflects collective psychology and short-term dynamics", 
                "3. **On-chain metrics** reveal actual network usage and fundamentals",
                "",
                "Understanding these relationships helps develop market awareness and ",
                "critical thinking skills. However, remember that markets remain inherently ",
                "unpredictable, and historical patterns don't guarantee future outcomes.",
                "",
                "The goal is education, not prediction. Use these insights to become a ",
                "more informed market participant, not as a basis for trading decisions."
            ]
            
            return "\n".join(context_parts)
            
        except Exception as e:
            logger.error(f"Error formatting educational context: {str(e)}")
            return "Educational context unavailable due to formatting error."
    
    def _get_market_state_explanation(self, state: str) -> str:
        """
        Get explanation for market state.
        
        Args:
            state: Market state (positive, negative, neutral)
            
        Returns:
            Explanation string
        """
        explanations = {
            "positive": "Market conditions appear favorable, though this doesn't guarantee future performance.",
            "negative": "Market conditions appear challenging, though markets can recover unexpectedly.",
            "neutral": "Market conditions show mixed signals, suggesting uncertainty in the short term."
        }
        
        return explanations.get(state, "Market conditions are currently being assessed.")
    
    def _format_metadata(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format response metadata.
        
        Args:
            analysis_data: Complete analysis data
            
        Returns:
            Formatted metadata
        """
        try:
            return {
                "analysis_timestamp": analysis_data.get("timestamp", self._get_timestamp()),
                "assets_analyzed": analysis_data.get("assets_analyzed", []),
                "analysis_types": ["macroeconomic", "sentiment", "onchain"],
                "confidence_level": "moderate",
                "data_sources": "Educational/Conceptual",
                "limitations": [
                    "Analysis is educational and conceptual",
                    "No real-time market data is used",
                    "Not suitable for trading decisions",
                    "Markets remain inherently unpredictable"
                ]
            }
        except Exception as e:
            logger.error(f"Error formatting metadata: {str(e)}")
            return {"error": "Metadata formatting failed"}
    
    def _get_standard_disclaimer(self) -> str:
        """
        Get standard disclaimer for all responses.
        
        Returns:
            Disclaimer string
        """
        return (
            "⚠️ **IMPORTANT DISCLAIMER**\n\n"
            "This analysis is for **educational and informational purposes only**. "
            "It does **not** constitute financial advice, investment recommendations, "
            "price predictions, or trading signals.\n\n"
            "Cryptocurrency markets are **highly volatile and risky**. Prices can "
            "fluctuate dramatically, and you may lose all of your invested capital.\n\n"
            "**Always conduct your own research** and consult with qualified financial "
            "professionals before making any investment decisions. Past performance does "
            "not indicate future results.\n\n"
            "This tool is designed to help you **understand market dynamics**, not to "
            "tell you when to buy or sell. Use these insights to become a more informed "
            "market participant, not as a basis for financial decisions."
        )
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        return datetime.utcnow().isoformat() + "Z"
    
    def _error_response(self, query: str, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "query": query,
            "timestamp": self._get_timestamp(),
            "error": True,
            "message": f"Response formatting failed: {error_message}",
            "disclaimer": self._get_standard_disclaimer()
        }
    
    def format_simple_response(self, message: str, include_disclaimer: bool = True) -> str:
        """
        Format a simple text response.
        
        Args:
            message: Message to format
            include_disclaimer: Whether to include disclaimer
            
        Returns:
            Formatted response string
        """
        try:
            response_parts = [message]
            
            if include_disclaimer:
                response_parts.extend([
                    "",
                    self._get_standard_disclaimer()
                ])
            
            return "\n".join(response_parts)
            
        except Exception as e:
            logger.error(f"Error formatting simple response: {str(e)}")
            return f"{message}\n\n[Response formatting error occurred]"
