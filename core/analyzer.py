"""
Main analysis orchestrator for MacroChain AI.

This module combines insights from macro, sentiment, and on-chain analysis
to provide comprehensive cryptocurrency market analysis.
"""

from typing import Dict, Any, List
import logging
from .macro import MacroAnalyzer
from .sentiment import SentimentAnalyzer
from .onchain import OnChainAnalyzer
from .market_structure import MarketStructureAnalyzer
from .research_pipeline import ResearchPipeline


logger = logging.getLogger(__name__)


class MacroChainAnalyzer:
    """
    Main analyzer that orchestrates all analysis components.
    
    This class combines macroeconomic, sentiment, and on-chain analysis
    to provide comprehensive market insights while maintaining an
    educational and neutral perspective.
    """
    
    def __init__(self):
        """Initialize the analyzer with all components."""
        self.macro_analyzer = MacroAnalyzer()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.onchain_analyzer = OnChainAnalyzer()
        self.market_structure_analyzer = MarketStructureAnalyzer()
        self.research_pipeline = ResearchPipeline()
        
    def analyze(self, query: str, assets: List[str] = None) -> Dict[str, Any]:
        """
        Perform comprehensive market analysis using the research pipeline.
        
        Args:
            query: User's analysis request
            assets: List of assets to focus on (optional)
            
        Returns:
            Dictionary containing structured analysis results
        """
        try:
            logger.info(f"Starting comprehensive analysis for query: {query}")
            
            # Use the research pipeline for comprehensive analysis
            pipeline_result = self.research_pipeline.execute_research(query, assets)
            
            if pipeline_result.get("error"):
                return self._error_response(pipeline_result.get("message", "Pipeline failed"))
            
            # Format results for backward compatibility
            formatted_result = self._format_pipeline_results(pipeline_result)
            
            logger.info("Comprehensive analysis completed successfully")
            return formatted_result
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            return self._error_response(str(e))
    
    def analyze_legacy(self, query: str, assets: List[str] = None) -> Dict[str, Any]:
        """
        Legacy analysis method for backward compatibility.
        
        Args:
            query: User's analysis request
            assets: List of assets to focus on (optional)
            
        Returns:
            Dictionary containing structured analysis results
        """
        try:
            logger.info(f"Starting legacy analysis for query: {query}")
            
            # Default to major cryptocurrencies if no assets specified
            if not assets:
                assets = ["bitcoin", "ethereum"]
            
            # Perform individual analyses
            macro_analysis = self.macro_analyzer.analyze(query, assets)
            sentiment_analysis = self.sentiment_analyzer.analyze(query, assets)
            onchain_analysis = self.onchain_analyzer.analyze(query, assets)
            structure_analysis = self.market_structure_analyzer.analyze(query, assets)
            
            # Combine insights
            combined_analysis = self._combine_analyses(
                macro_analysis,
                sentiment_analysis, 
                onchain_analysis,
                structure_analysis,
                query,
                assets
            )
            
            logger.info("Legacy analysis completed successfully")
            return combined_analysis
            
        except Exception as e:
            logger.error(f"Error during legacy analysis: {str(e)}")
            return self._error_response(str(e))
    
    def _combine_analyses(
        self, 
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any],
        query: str,
        assets: List[str]
    ) -> Dict[str, Any]:
        """
        Combine individual analyses into a comprehensive result.
        
        Args:
            macro: Macroeconomic analysis results
            sentiment: Sentiment analysis results
            onchain: On-chain analysis results
            structure: Market structure analysis results
            query: Original user query
            assets: Assets analyzed
            
        Returns:
            Combined analysis dictionary
        """
        # Extract key insights from each analysis
        macro_insights = macro.get("insights", [])
        sentiment_insights = sentiment.get("insights", [])
        onchain_insights = onchain.get("insights", [])
        structure_insights = structure.get("insights", [])
        
        # Identify themes and correlations
        themes = self._identify_themes(macro, sentiment, onchain, structure)
        correlations = self._find_correlations(macro, sentiment, onchain, structure)
        
        # Assess overall market conditions
        market_conditions = self._assess_market_conditions(
            macro, sentiment, onchain, structure
        )
        
        # Generate educational summary
        educational_summary = self._generate_educational_summary(
            query, assets, themes, correlations
        )
        
        return {
            "query": query,
            "assets_analyzed": assets,
            "timestamp": self._get_timestamp(),
            "market_conditions": market_conditions,
            "macro_analysis": macro,
            "sentiment_analysis": sentiment,
            "onchain_analysis": onchain,
            "market_structure_analysis": structure,
            "key_themes": themes,
            "correlations": correlations,
            "educational_summary": educational_summary,
            "risk_factors": self._identify_risk_factors(macro, sentiment, onchain, structure),
            "disclaimer": self._get_disclaimer()
        }
    
    def _identify_themes(
        self, 
        macro: Dict[str, Any],
        sentiment: Dict[str, Any], 
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[str]:
        """
        Identify recurring themes across different analyses.
        
        Args:
            macro: Macroeconomic analysis
            sentiment: Sentiment analysis
            onchain: On-chain analysis
            structure: Market structure analysis
            
        Returns:
            List of identified themes
        """
        themes = []
        
        # Check for liquidity themes
        if (macro.get("liquidity_tightening") or 
            onchain.get("reduced_activity") or
            structure.get("liquidity_conditions", {}).get("current_condition") == "tight"):
            themes.append("Liquidity conditions affecting market activity")
        
        # Check for sentiment themes
        if (sentiment.get("fear_dominance") or 
            sentiment.get("risk_off_sentiment")):
            themes.append("Risk aversion dominating market sentiment")
        
        # Check for network activity themes
        if (onchain.get("increased_adoption") or 
            onchain.get("network_growth")):
            themes.append("Network fundamentals showing strength")
        
        # Check for macro uncertainty
        if (macro.get("policy_uncertainty") or 
            macro.get("economic_volatility")):
            themes.append("Macroeconomic uncertainty influencing crypto markets")
        
        # Check for market structure themes
        structure_phase = structure.get("market_phase", {}).get("current_phase")
        if structure_phase in ["transition", "uncertain"]:
            themes.append("Market structure in transition phase")
        elif structure_phase in ["trend_up", "trend_down"]:
            themes.append("Defined market structure with directional bias")
        
        return themes
    
    def _find_correlations(
        self, 
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Find correlations between different analysis types.
        
        Args:
            macro: Macroeconomic analysis
            sentiment: Sentiment analysis
            onchain: On-chain analysis
            structure: Market structure analysis
            
        Returns:
            List of correlation observations
        """
        correlations = []
        
        # Correlate macro liquidity with on-chain activity
        if (macro.get("liquidity_conditions") == "tight" and 
            onchain.get("transaction_volume_trend") == "decreasing"):
            correlations.append({
                "type": "macro_onchain",
                "observation": "Tight macro liquidity correlates with reduced on-chain activity",
                "strength": "moderate"
            })
        
        # Correlate sentiment with market activity
        if (sentiment.get("overall_sentiment") == "fear" and 
            onchain.get("holder_behavior") == "accumulation"):
            correlations.append({
                "type": "sentiment_onchain",
                "observation": "Fear sentiment coincides with long-term holder accumulation",
                "strength": "moderate"
            })
        
        # Correlate market structure with volatility
        structure_phase = structure.get("market_phase", {}).get("current_phase")
        volatility_regime = structure.get("volatility_regime", {}).get("current_regime")
        
        if (structure_phase == "transition" and 
            volatility_regime in ["high", "extreme"]):
            correlations.append({
                "type": "structure_volatility",
                "observation": "Market structure transition coincides with high volatility",
                "strength": "strong"
            })
        
        # Correlate macro conditions with market structure
        if (macro.get("overall_conditions", {}).get("overall") == "challenging" and
            structure.get("market_phase", {}).get("current_phase") == "range"):
            correlations.append({
                "type": "macro_structure",
                "observation": "Challenging macro conditions coincide with range-bound structure",
                "strength": "moderate"
            })
        
        return correlations
    
    def _assess_market_conditions(
        self, 
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess overall market conditions based on all analyses.
        
        Args:
            macro: Macroeconomic analysis
            sentiment: Sentiment analysis
            onchain: On-chain analysis
            structure: Market structure analysis
            
        Returns:
            Market conditions assessment
        """
        conditions = {
            "overall_state": "neutral",
            "key_factors": [],
            "confidence_level": "moderate"
        }
        
        # Determine overall state
        factors = []
        
        if sentiment.get("overall_sentiment") == "fear":
            factors.append("Negative sentiment pressure")
        elif sentiment.get("overall_sentiment") == "greed":
            factors.append("Positive sentiment pressure")
        
        if macro.get("liquidity_conditions") == "tight":
            factors.append("Constrained macro liquidity")
        elif macro.get("liquidity_conditions") == "ample":
            factors.append("Supportive macro liquidity")
        
        if onchain.get("network_health") == "strong":
            factors.append("Strong on-chain fundamentals")
        elif onchain.get("network_health") == "weakening":
            factors.append("Weakening on-chain fundamentals")
        
        # Add market structure factors
        structure_phase = structure.get("market_phase", {}).get("current_phase")
        if structure_phase in ["trend_up", "trend_down"]:
            factors.append(f"Defined {structure_phase.replace('_', ' ')} structure")
        elif structure_phase == "transition":
            factors.append("Market structure in transition")
        
        volatility_regime = structure.get("volatility_regime", {}).get("current_regime")
        if volatility_regime in ["high", "extreme"]:
            factors.append("High volatility environment")
        elif volatility_regime == "low":
            factors.append("Low volatility environment")
        
        conditions["key_factors"] = factors
        
        # Set overall state based on balance of factors
        positive_factors = sum(1 for f in factors if "positive" in f.lower() or "strong" in f.lower() or "supportive" in f.lower() or "trend_up" in f.lower())
        negative_factors = sum(1 for f in factors if "negative" in f.lower() or "weakening" in f.lower() or "constrained" in f.lower() or "trend_down" in f.lower())
        
        if positive_factors > negative_factors:
            conditions["overall_state"] = "positive"
        elif negative_factors > positive_factors:
            conditions["overall_state"] = "negative"
        else:
            conditions["overall_state"] = "neutral"
        
        return conditions
    
    def _generate_educational_summary(
        self, 
        query: str,
        assets: List[str],
        themes: List[str],
        correlations: List[Dict[str, Any]]
    ) -> str:
        """
        Generate an educational summary of the analysis.
        
        Args:
            query: Original user query
            assets: Assets analyzed
            themes: Identified themes
            correlations: Found correlations
            
        Returns:
            Educational summary string
        """
        summary_parts = [
            f"Analysis of {', '.join(assets)} based on your query about {query}.",
            ""
        ]
        
        if themes:
            summary_parts.append("Key market themes identified:")
            for theme in themes:
                summary_parts.append(f"- {theme}")
            summary_parts.append("")
        
        if correlations:
            summary_parts.append("Notable market correlations:")
            for corr in correlations:
                summary_parts.append(f"- {corr['observation']}")
            summary_parts.append("")
        
        summary_parts.extend([
            "This analysis illustrates how different factors interact in cryptocurrency markets.",
            "Understanding these relationships can help in developing market awareness,",
            "though it's important to remember that markets remain inherently unpredictable.",
            ""
        ])
        
        return "\n".join(summary_parts)
    
    def _identify_risk_factors(
        self, 
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[str]:
        """
        Identify key risk factors from the analysis.
        
        Args:
            macro: Macroeconomic analysis
            sentiment: Sentiment analysis
            onchain: On-chain analysis
            structure: Market structure analysis
            
        Returns:
            List of risk factors
        """
        risks = []
        
        if macro.get("policy_uncertainty"):
            risks.append("Regulatory and policy uncertainty")
        
        if sentiment.get("extreme_sentiment"):
            risks.append("Extreme market sentiment may indicate volatility")
        
        if onchain.get("concentration_risk"):
            risks.append("High concentration of holdings")
        
        if macro.get("liquidity_conditions") == "tight":
            risks.append("Reduced market liquidity")
        
        # Add market structure risks
        structure_phase = structure.get("market_phase", {}).get("current_phase")
        if structure_phase == "transition":
            risks.append("Market structure transition increases uncertainty")
        
        volatility_regime = structure.get("volatility_regime", {}).get("current_regime")
        if volatility_regime in ["high", "extreme"]:
            risks.append("High volatility environment increases risk")
        
        liquidity_condition = structure.get("liquidity_conditions", {}).get("current_condition")
        if liquidity_condition in ["tight", "very_tight"]:
            risks.append("Tight liquidity conditions may increase execution risk")
        
        # Always include general market risk
        risks.append("General cryptocurrency market volatility")
        
        return risks
    
    def _format_pipeline_results(self, pipeline_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format pipeline results for backward compatibility.
        
        Args:
            pipeline_result: Results from research pipeline
            
        Returns:
            Formatted results compatible with existing API
        """
        research_findings = pipeline_result.get("research_findings", {})
        phase_results = pipeline_result.get("phase_results", {})
        
        # Extract individual phase results
        macro_analysis = phase_results.get("macro", {})
        sentiment_analysis = phase_results.get("sentiment", {})
        onchain_analysis = phase_results.get("onchain", {})
        structure_analysis = phase_results.get("market_structure", {})
        
        return {
            "query": pipeline_result["research_metadata"]["query"],
            "assets_analyzed": pipeline_result["research_metadata"]["assets_analyzed"],
            "timestamp": pipeline_result["research_metadata"]["timestamp"],
            "market_conditions": {
                "overall_state": research_findings.get("overall_market_state", {}).get("overall_state", "neutral"),
                "key_factors": research_findings.get("overall_market_state", {}).get("dominant_factors", []),
                "confidence_level": research_findings.get("confidence_level", "moderate")
            },
            "macro_analysis": macro_analysis,
            "sentiment_analysis": sentiment_analysis,
            "onchain_analysis": onchain_analysis,
            "market_structure_analysis": structure_analysis,
            "key_themes": [corr.get("observation", "") for corr in research_findings.get("cross_phase_correlations", [])],
            "correlations": research_findings.get("cross_phase_correlations", []),
            "educational_summary": f"Comprehensive research analysis completed with {research_findings.get('total_insights', 0)} insights identified.",
            "risk_factors": pipeline_result.get("limitations", []),
            "research_quality": research_findings.get("research_quality", {}),
            "disclaimer": pipeline_result.get("disclaimer", self._get_disclaimer())
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for analysis."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    
    def _get_disclaimer(self) -> str:
        """Get standard disclaimer for analysis."""
        return (
            "This analysis is for educational purposes only and does not constitute "
            "financial advice. Cryptocurrency markets are highly volatile and risky. "
            "Always conduct your own research and consult with qualified financial "
            "professionals before making any investment decisions."
        )
    
    def _error_response(self, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "error": True,
            "message": f"Analysis failed: {error_message}",
            "disclaimer": self._get_disclaimer()
        }
