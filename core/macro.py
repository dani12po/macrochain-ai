"""
Macroeconomic analysis module for MacroChain AI.

This module handles the analysis of macroeconomic factors that influence
cryptocurrency markets, including liquidity, interest rates, and global
risk sentiment.
"""

from typing import Dict, Any, List
import logging


logger = logging.getLogger(__name__)


class MacroAnalyzer:
    """
    Analyzes macroeconomic factors affecting cryptocurrency markets.
    
    This class provides educational analysis of how traditional macroeconomic
    indicators and policies influence cryptocurrency market dynamics.
    """
    
    def __init__(self):
        """Initialize the macro analyzer."""
        self.macro_indicators = [
            "interest_rates",
            "inflation", 
            "liquidity_conditions",
            "economic_growth",
            "risk_sentiment",
            "regulatory_environment"
        ]
    
    def analyze(self, query: str, assets: List[str] = None) -> Dict[str, Any]:
        """
        Perform macroeconomic analysis based on the query.
        
        Args:
            query: User's analysis request
            assets: List of assets to focus on (optional)
            
        Returns:
            Dictionary containing macroeconomic analysis results
        """
        try:
            logger.info(f"Starting macro analysis for query: {query}")
            
            # Analyze different macro factors
            liquidity_analysis = self._analyze_liquidity_conditions()
            interest_rate_analysis = self._analyze_interest_rate_environment()
            risk_sentiment_analysis = self._analyze_global_risk_sentiment()
            regulatory_analysis = self._analyze_regulatory_environment()
            
            # Generate insights
            insights = self._generate_macro_insights(
                liquidity_analysis,
                interest_rate_analysis,
                risk_sentiment_analysis,
                regulatory_analysis
            )
            
            # Assess overall macro conditions
            macro_conditions = self._assess_macro_conditions(
                liquidity_analysis,
                interest_rate_analysis,
                risk_sentiment_analysis
            )
            
            result = {
                "analysis_type": "macroeconomic",
                "liquidity_conditions": liquidity_analysis,
                "interest_rate_environment": interest_rate_analysis,
                "global_risk_sentiment": risk_sentiment_analysis,
                "regulatory_environment": regulatory_analysis,
                "overall_conditions": macro_conditions,
                "insights": insights,
                "educational_notes": self._get_educational_notes(),
                "timestamp": self._get_timestamp()
            }
            
            logger.info("Macro analysis completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error in macro analysis: {str(e)}")
            return self._error_response(str(e))
    
    def _analyze_liquidity_conditions(self) -> Dict[str, Any]:
        """
        Analyze global liquidity conditions affecting crypto markets.
        
        Returns:
            Dictionary with liquidity analysis
        """
        # Educational analysis of liquidity factors
        liquidity_factors = {
            "central_bank_policies": {
                "status": "accommodative",  # Educational placeholder
                "impact": "Central bank balance sheets affect global liquidity",
                "explanation": "When central banks expand balance sheets through quantitative easing, it typically increases available liquidity that can flow into various asset classes, including cryptocurrencies."
            },
            "dollar_strength": {
                "status": "neutral",
                "impact": "Strong dollar can pressure crypto prices",
                "explanation": "A stronger US dollar typically makes dollar-denominated assets more expensive for international investors, potentially reducing demand for cryptocurrencies."
            },
            "credit_conditions": {
                "status": "moderate",
                "impact": "Credit availability influences risk asset demand",
                "explanation": "Loose credit conditions often correlate with higher demand for risk assets like cryptocurrencies, while tight credit conditions can reduce investment flows."
            }
        }
        
        overall_liquidity = self._assess_overall_liquidity(liquidity_factors)
        
        return {
            "factors": liquidity_factors,
            "overall_status": overall_liquidity,
            "trend": "stable",  # Educational placeholder
            "key_observations": [
                "Global liquidity remains a key driver of crypto market cycles",
                "Liquidity changes often precede price movements in crypto markets",
                "Cross-asset liquidity correlations are important to monitor"
            ]
        }
    
    def _analyze_interest_rate_environment(self) -> Dict[str, Any]:
        """
        Analyze interest rate environment and its impact on crypto.
        
        Returns:
            Dictionary with interest rate analysis
        """
        rate_factors = {
            "policy_rates": {
                "current_trend": "stable",  # Educational placeholder
                "impact": "Higher rates can reduce demand for risk assets",
                "explanation": "When interest rates rise, traditional savings become more attractive, potentially reducing the relative appeal of cryptocurrencies as alternative investments."
            },
            "real_rates": {
                "status": "negative_to_neutral",
                "impact": "Negative real rates historically support crypto",
                "explanation": "When inflation exceeds nominal interest rates, investors may seek assets like cryptocurrencies that can potentially preserve purchasing power."
            },
            "yield_curve": {
                "shape": "normal",
                "impact": "Yield curve shape indicates economic expectations",
                "explanation": "The yield curve reflects market expectations about future economic conditions and can influence risk appetite across all asset classes."
            }
        }
        
        rate_implications = self._assess_rate_implications(rate_factors)
        
        return {
            "factors": rate_factors,
            "implications": rate_implications,
            "trend": "monitoring",
            "educational_context": [
                "Interest rates are a fundamental driver of asset allocation decisions",
                "Cryptocurrencies often behave like high-duration assets in rate environments",
                "Rate expectations can be more important than current rates"
            ]
        }
    
    def _analyze_global_risk_sentiment(self) -> Dict[str, Any]:
        """
        Analyze global risk sentiment and risk appetite.
        
        Returns:
            Dictionary with risk sentiment analysis
        """
        sentiment_indicators = {
            "equity_markets": {
                "trend": "cautious",
                "impact": "Equity performance often correlates with crypto",
                "explanation": "Cryptocurrencies, particularly Bitcoin, have shown increasing correlation with broader risk assets, especially during periods of market stress."
            },
            "volatility_indices": {
                "level": "moderate",
                "impact": "Higher volatility indicates increased fear",
                "explanation": "Traditional volatility indices like the VIX can serve as proxies for overall market risk appetite, which often extends to cryptocurrency markets."
            },
            "safe_haven_demand": {
                "status": "balanced",
                "impact": "Safe haven demand affects risk asset flows",
                "explanation": "During periods of heightened uncertainty, investors may rotate between safe havens and risk assets, impacting cryptocurrency demand patterns."
            }
        }
        
        overall_sentiment = self._assess_overall_sentiment(sentiment_indicators)
        
        return {
            "indicators": sentiment_indicators,
            "overall_sentiment": overall_sentiment,
            "risk_appetite": "moderate",
            "key_insights": [
                "Risk sentiment is a major driver of short-term crypto price movements",
                "Cryptocurrency's role as risk asset vs safe haven continues to evolve",
                "Global risk flows increasingly interconnected across asset classes"
            ]
        }
    
    def _analyze_regulatory_environment(self) -> Dict[str, Any]:
        """
        Analyze regulatory environment affecting cryptocurrencies.
        
        Returns:
            Dictionary with regulatory analysis
        """
        regulatory_factors = {
            "major_jurisdictions": {
                "trend": "clarification_increasing",
                "impact": "Regulatory clarity can support institutional adoption",
                "explanation": "Clear regulatory frameworks reduce uncertainty for institutional investors and can support market development."
            },
            "compliance_requirements": {
                "status": "evolving",
                "impact": "Compliance costs affect market participants",
                "explanation": "Increasing compliance requirements can impact operational costs for crypto businesses and influence market structure."
            },
            "international_coordination": {
                "level": "improving",
                "impact": "Coordinated approaches reduce regulatory arbitrage",
                "explanation": "Better international coordination on crypto regulation can create more consistent global market conditions."
            }
        }
        
        regulatory_outlook = self._assess_regulatory_outlook(regulatory_factors)
        
        return {
            "factors": regulatory_factors,
            "outlook": regulatory_outlook,
            "focus_areas": [
                "Institutional adoption frameworks",
                "Consumer protection measures",
                "Market structure regulations",
                "Cross-border coordination"
            ]
        }
    
    def _generate_macro_insights(
        self,
        liquidity: Dict[str, Any],
        rates: Dict[str, Any],
        sentiment: Dict[str, Any],
        regulatory: Dict[str, Any]
    ) -> List[str]:
        """
        Generate key insights from macro analysis.
        
        Args:
            liquidity: Liquidity analysis results
            rates: Interest rate analysis results
            sentiment: Risk sentiment analysis results
            regulatory: Regulatory analysis results
            
        Returns:
            List of key insights
        """
        insights = []
        
        # Liquidity insights
        if liquidity["overall_status"] == "tight":
            insights.append("Tight liquidity conditions may constrain crypto market growth")
        elif liquidity["overall_status"] == "ample":
            insights.append("Supportive liquidity environment could benefit crypto markets")
        
        # Rate insights
        if rates["implications"]["overall"] == "challenging":
            insights.append("Current interest rate environment presents headwinds for risk assets")
        elif rates["implications"]["overall"] == "supportive":
            insights.append("Interest rate conditions appear supportive for crypto markets")
        
        # Sentiment insights
        if sentiment["overall_sentiment"]["status"] == "risk_off":
            insights.append("Risk-off sentiment may pressure crypto prices in short term")
        elif sentiment["overall_sentiment"]["status"] == "risk_on":
            insights.append("Risk-on environment could support crypto market performance")
        
        # Regulatory insights
        if regulatory["outlook"]["trend"] == "positive":
            insights.append("Evolving regulatory clarity may support institutional adoption")
        
        return insights
    
    def _assess_macro_conditions(
        self,
        liquidity: Dict[str, Any],
        rates: Dict[str, Any],
        sentiment: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess overall macroeconomic conditions.
        
        Args:
            liquidity: Liquidity analysis
            rates: Interest rate analysis
            sentiment: Risk sentiment analysis
            
        Returns:
            Overall macro conditions assessment
        """
        conditions = {
            "overall": "neutral",
            "key_drivers": [],
            "outlook": "uncertain"
        }
        
        # Determine key drivers
        if liquidity["overall_status"] == "tight":
            conditions["key_drivers"].append("Liquidity constraints")
        
        if rates["implications"]["overall"] == "challenging":
            conditions["key_drivers"].append("Unfavorable rate environment")
        
        if sentiment["overall_sentiment"]["status"] == "risk_off":
            conditions["key_drivers"].append("Risk aversion")
        
        # Set overall assessment
        if len(conditions["key_drivers"]) >= 2:
            conditions["overall"] = "challenging"
        elif len(conditions["key_drivers"]) == 1:
            conditions["overall"] = "mixed"
        else:
            conditions["overall"] = "supportive"
        
        return conditions
    
    def _assess_overall_liquidity(self, factors: Dict[str, Any]) -> str:
        """Assess overall liquidity conditions."""
        # Simplified logic for educational purposes
        return "neutral"
    
    def _assess_rate_implications(self, factors: Dict[str, Any]) -> Dict[str, Any]:
        """Assess implications of interest rate environment."""
        return {
            "overall": "neutral",
            "key_considerations": [
                "Rate expectations matter more than current rates",
                "Real rates impact investment decisions",
                "Policy divergence creates complexity"
            ]
        }
    
    def _assess_overall_sentiment(self, indicators: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall risk sentiment."""
        return {
            "status": "neutral",
            "confidence": "moderate",
            "factors": "Mixed signals across different indicators"
        }
    
    def _assess_regulatory_outlook(self, factors: Dict[str, Any]) -> Dict[str, Any]:
        """Assess regulatory outlook."""
        return {
            "trend": "neutral",
            "certainty": "increasing",
            "key_developments": "Continued framework development"
        }
    
    def _get_educational_notes(self) -> List[str]:
        """Get educational notes about macro analysis."""
        return [
            "Macroeconomic factors provide context for cryptocurrency market movements",
            "Traditional market relationships with crypto are evolving over time",
            "Global liquidity cycles often correlate with crypto market cycles",
            "Interest rate environments influence relative attractiveness of different assets",
            "Regulatory development is a key factor in long-term market maturation"
        ]
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    
    def _error_response(self, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "error": True,
            "message": f"Macro analysis failed: {error_message}",
            "educational_notes": self._get_educational_notes()
        }
