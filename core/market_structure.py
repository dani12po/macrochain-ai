"""
Market Structure Analysis for MacroChain AI.

This module provides crypto trading context analysis without providing
trading signals or financial advice. Focus is on market structure,
phase classification, and risk context.
"""

from typing import Dict, Any, List, Optional
import logging
from enum import Enum
from dataclasses import dataclass


logger = logging.getLogger(__name__)


class MarketPhase(Enum):
    """Market phase classification."""
    TREND_UP = "trend_up"
    TREND_DOWN = "trend_down"
    RANGE = "range"
    TRANSITION = "transition"
    UNCERTAIN = "uncertain"


class VolatilityRegime(Enum):
    """Volatility regime classification."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    EXTREME = "extreme"


class LiquidityCondition(Enum):
    """Liquidity condition classification."""
    AMPLE = "ample"
    MODERATE = "moderate"
    TIGHT = "tight"
    VERY_TIGHT = "very_tight"


@dataclass
class MarketStructureMetrics:
    """Market structure metrics."""
    phase: MarketPhase
    volatility_regime: VolatilityRegime
    liquidity_condition: LiquidityCondition
    trend_strength: str
    market_efficiency: str
    structural_biases: List[str]


class MarketStructureAnalyzer:
    """
    Analyzes market structure for crypto trading context.
    
    This class provides educational analysis of market structure without
    providing trading signals, recommendations, or financial advice.
    """
    
    def __init__(self):
        """Initialize the market structure analyzer."""
        self.structure_factors = [
            "price_action",
            "volume_patterns",
            "volatility_characteristics",
            "liquidity_analysis",
            "market_participation",
            "structural_biases"
        ]
    
    def analyze(self, query: str, assets: List[str] = None) -> Dict[str, Any]:
        """
        Perform market structure analysis based on the query.
        
        Args:
            query: User's analysis request
            assets: List of assets to focus on (optional)
            
        Returns:
            Dictionary containing market structure analysis results
        """
        try:
            logger.info(f"Starting market structure analysis for query: {query}")
            
            # Default to major cryptocurrencies if no assets specified
            if not assets:
                assets = ["bitcoin", "ethereum"]
            
            # Analyze different structure components
            phase_analysis = self._analyze_market_phase(query, assets)
            volatility_analysis = self._analyze_volatility_regime(query, assets)
            liquidity_analysis = self._analyze_liquidity_conditions(query, assets)
            efficiency_analysis = self._analyze_market_efficiency(query, assets)
            
            # Generate structural insights
            insights = self._generate_structure_insights(
                phase_analysis,
                volatility_analysis,
                liquidity_analysis,
                efficiency_analysis
            )
            
            # Assess overall market structure
            structure_assessment = self._assess_market_structure(
                phase_analysis,
                volatility_analysis,
                liquidity_analysis,
                efficiency_analysis
            )
            
            result = {
                "analysis_type": "market_structure",
                "market_phase": phase_analysis,
                "volatility_regime": volatility_analysis,
                "liquidity_conditions": liquidity_analysis,
                "market_efficiency": efficiency_analysis,
                "structure_assessment": structure_assessment,
                "insights": insights,
                "educational_context": self._get_educational_context(),
                "assumptions": self._get_assumptions(),
                "limitations": self._get_limitations(),
                "timestamp": self._get_timestamp()
            }
            
            logger.info("Market structure analysis completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error in market structure analysis: {str(e)}")
            return self._error_response(str(e))
    
    def _analyze_market_phase(self, query: str, assets: List[str]) -> Dict[str, Any]:
        """
        Analyze current market phase.
        
        Args:
            query: User's analysis request
            assets: Assets to analyze
            
        Returns:
            Market phase analysis
        """
        # Educational analysis of market phase characteristics
        phase_indicators = {
            "price_characteristics": {
                "directional_bias": "neutral",  # Educational placeholder
                "momentum_quality": "moderate",
                "trend_consistency": "variable",
                "explanation": "Price characteristics help identify whether markets are trending, ranging, or in transition."
            },
            "volume_patterns": {
                "volume_trend": "stable",
                "volume_quality": "moderate",
                "participation_level": "moderate",
                "explanation": "Volume analysis provides insights into market conviction and participation strength."
            },
            "range_boundaries": {
                "support_resistance": "identifiable",
                "range_width": "moderate",
                "boundary_strength": "moderate",
                "explanation": "Range boundaries indicate areas of buying/selling interest and potential support/resistance."
            },
            "transition_signals": {
                "phase_shift_probability": "moderate",
                "transition_clarity": "unclear",
                "breakout_potential": "balanced",
                "explanation": "Transition signals help identify potential phase changes in market structure."
            }
        }
        
        # Determine market phase
        market_phase = self._classify_market_phase(phase_indicators)
        phase_confidence = self._assess_phase_confidence(phase_indicators)
        
        return {
            "current_phase": market_phase,
            "phase_confidence": phase_confidence,
            "indicators": phase_indicators,
            "phase_characteristics": self._get_phase_characteristics(market_phase),
            "transition_risks": self._identify_transition_risks(market_phase, phase_indicators),
            "educational_notes": [
                "Market phases help contextualize price action and volatility patterns",
                "Phase identification is probabilistic, not deterministic",
                "Different assets can be in different phases simultaneously",
                "Phase transitions often coincide with volatility changes"
            ]
        }
    
    def _analyze_volatility_regime(self, query: str, assets: List[str]) -> Dict[str, Any]:
        """
        Analyze current volatility regime.
        
        Args:
            query: User's analysis request
            assets: Assets to analyze
            
        Returns:
            Volatility regime analysis
        """
        volatility_indicators = {
            "volatility_level": {
                "current_regime": "medium",  # Educational placeholder
                "historical_comparison": "near_average",
                "trend_direction": "stable",
                "explanation": "Volatility level indicates the magnitude of price fluctuations and market uncertainty."
            },
            "volatility_persistence": {
                "autocorrelation": "moderate",
                "regime_stability": "moderate",
                "mean_reversion_tendency": "present",
                "explanation": "Volatility persistence shows whether current conditions are likely to continue."
            },
            "volatility_skew": {
                "asymmetry": "slight_negative",
                "tail_risk": "moderate",
                "distribution_shape": "near_normal",
                "explanation": "Volatility skew reveals asymmetries in upside vs downside volatility potential."
            },
            "intraday_patterns": {
                "session_consistency": "moderate",
                "time_of_day_effects": "present",
                "gap_behavior": "moderate",
                "explanation": "Intraday patterns help understand volatility dynamics throughout trading sessions."
            }
        }
        
        # Classify volatility regime
        volatility_regime = self._classify_volatility_regime(volatility_indicators)
        regime_stability = self._assess_regime_stability(volatility_indicators)
        
        return {
            "current_regime": volatility_regime,
            "regime_stability": regime_stability,
            "indicators": volatility_indicators,
            "regime_characteristics": self._get_regime_characteristics(volatility_regime),
            "risk_implications": self._assess_volatility_risks(volatility_regime, volatility_indicators),
            "educational_context": [
                "Volatility regimes influence risk management and position sizing considerations",
                "Different regimes favor different types of market participants",
                "Volatility clustering is common in crypto markets",
                "Regime transitions often present both risks and opportunities"
            ]
        }
    
    def _analyze_liquidity_conditions(self, query: str, assets: List[str]) -> Dict[str, Any]:
        """
        Analyze market liquidity conditions.
        
        Args:
            query: User's analysis request
            assets: Assets to analyze
            
        Returns:
            Liquidity conditions analysis
        """
        liquidity_indicators = {
            "order_book_depth": {
                "depth_level": "moderate",
                "spread_tightness": "moderate",
                "depth_distribution": "balanced",
                "explanation": "Order book depth indicates available liquidity at different price levels."
            },
            "market_impact": {
                "impact_level": "moderate",
                "slippage_expectation": "moderate",
                "size_capacity": "moderate",
                "explanation": "Market impact shows how trade sizes affect prices, indicating liquidity quality."
            },
            "participation_diversity": {
                "participant_types": "diverse",
                "geographic_distribution": "global",
                "institutional_presence": "growing",
                "explanation": "Participation diversity affects liquidity stability and market resilience."
            },
            "temporal_patterns": {
                "session_liquidity": "variable",
                "day_of_week_effects": "present",
                "market_hours_impact": "significant",
                "explanation": "Temporal patterns reveal how liquidity varies across time periods."
            }
        }
        
        # Classify liquidity conditions
        liquidity_condition = self._classify_liquidity_condition(liquidity_indicators)
        liquidity_stability = self._assess_liquidity_stability(liquidity_indicators)
        
        return {
            "current_condition": liquidity_condition,
            "condition_stability": liquidity_stability,
            "indicators": liquidity_indicators,
            "condition_characteristics": self._get_liquidity_characteristics(liquidity_condition),
            "execution_considerations": self._assess_execution_considerations(liquidity_condition, liquidity_indicators),
            "educational_insights": [
                "Liquidity conditions affect transaction costs and market efficiency",
                "Liquidity can vary significantly across different cryptocurrencies",
                "Market stress often coincides with liquidity deterioration",
                "Understanding liquidity helps manage execution risk"
            ]
        }
    
    def _analyze_market_efficiency(self, query: str, assets: List[str]) -> Dict[str, Any]:
        """
        Analyze market efficiency and structural biases.
        
        Args:
            query: User's analysis request
            assets: Assets to analyze
            
        Returns:
            Market efficiency analysis
        """
        efficiency_indicators = {
            "information_flow": {
                "price_discovery": "moderate",
                "news_incorporation": "reasonable",
                "cross_market_arbitrage": "present",
                "explanation": "Information flow efficiency shows how quickly markets process new information."
            },
            "structural_biases": {
                "seasonal_patterns": "present",
                "day_of_week_effects": "mild",
                "holiday_effects": "present",
                "explanation": "Structural biases are recurring patterns that may indicate market inefficiencies."
            },
            "market_microstructure": {
                "tick_size_impact": "moderate",
                "lot_size_effects": "present",
                "trading_frictions": "moderate",
                "explanation": "Market microstructure affects how efficiently prices are formed and updated."
            },
            "behavioral_patterns": {
                "herding_behavior": "present",
                "overreaction_tendencies": "present",
                "mean_reversion": "present",
                "explanation": "Behavioral patterns can create predictable but temporary market inefficiencies."
            }
        }
        
        # Assess overall efficiency
        efficiency_level = self._assess_efficiency_level(efficiency_indicators)
        structural_biases = self._identify_structural_biases(efficiency_indicators)
        
        return {
            "efficiency_level": efficiency_level,
            "structural_biases": structural_biases,
            "indicators": efficiency_indicators,
            "efficiency_characteristics": self._get_efficiency_characteristics(efficiency_level),
            "bias_implications": self._assess_bias_implications(structural_biases),
            "educational_context": [
                "Market efficiency affects how quickly prices reflect available information",
                "Structural biases can create exploitable but risky patterns",
                "Crypto markets may have different efficiency characteristics than traditional markets",
                "Efficiency can vary across different cryptocurrencies and market conditions"
            ]
        }
    
    def _generate_structure_insights(
        self,
        phase: Dict[str, Any],
        volatility: Dict[str, Any],
        liquidity: Dict[str, Any],
        efficiency: Dict[str, Any]
    ) -> List[str]:
        """
        Generate key insights from market structure analysis.
        
        Args:
            phase: Market phase analysis
            volatility: Volatility regime analysis
            liquidity: Liquidity conditions analysis
            efficiency: Market efficiency analysis
            
        Returns:
            List of key insights
        """
        insights = []
        
        # Phase insights
        current_phase = phase.get("current_phase", "uncertain")
        if current_phase == MarketPhase.RANGE.value:
            insights.append("Range-bound market structure suggests defined support/resistance levels")
        elif current_phase in [MarketPhase.TREND_UP.value, MarketPhase.TREND_DOWN.value]:
            insights.append(f"Trending market structure indicates directional momentum")
        elif current_phase == MarketPhase.TRANSITION.value:
            insights.append("Transition phase suggests potential structural changes ahead")
        
        # Volatility insights
        volatility_regime = volatility.get("current_regime", "medium")
        if volatility_regime == VolatilityRegime.HIGH.value:
            insights.append("High volatility regime suggests increased uncertainty and risk")
        elif volatility_regime == VolatilityRegime.LOW.value:
            insights.append("Low volatility regime may indicate market complacency or consolidation")
        
        # Liquidity insights
        liquidity_condition = liquidity.get("current_condition", "moderate")
        if liquidity_condition == LiquidityCondition.TIGHT.value:
            insights.append("Tight liquidity conditions may increase execution costs and market impact")
        elif liquidity_condition == LiquidityCondition.AMPLE.value:
            insights.append("Ample liquidity conditions support efficient price discovery")
        
        # Efficiency insights
        efficiency_level = efficiency.get("efficiency_level", "moderate")
        if efficiency_level == "low":
            insights.append("Lower market efficiency may create temporary structural opportunities")
        elif efficiency_level == "high":
            insights.append("Higher market efficiency suggests prices quickly reflect available information")
        
        return insights
    
    def _assess_market_structure(
        self,
        phase: Dict[str, Any],
        volatility: Dict[str, Any],
        liquidity: Dict[str, Any],
        efficiency: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess overall market structure.
        
        Args:
            phase: Market phase analysis
            volatility: Volatility regime analysis
            liquidity: Liquidity conditions analysis
            efficiency: Market efficiency analysis
            
        Returns:
            Overall market structure assessment
        """
        structure_components = {
            "market_phase": phase.get("current_phase", "uncertain"),
            "volatility_regime": volatility.get("current_regime", "medium"),
            "liquidity_condition": liquidity.get("current_condition", "moderate"),
            "efficiency_level": efficiency.get("efficiency_level", "moderate")
        }
        
        # Assess overall structure quality
        structure_quality = self._assess_structure_quality(structure_components)
        risk_context = self._assess_structure_risk_context(structure_components)
        
        return {
            "overall_structure": structure_components,
            "structure_quality": structure_quality,
            "risk_context": risk_context,
            "structural_strengths": self._identify_structure_strengths(structure_components),
            "structural_concerns": self._identify_structure_concerns(structure_components),
            "market_maturity": self._assess_market_maturity(structure_components)
        }
    
    def _classify_market_phase(self, indicators: Dict[str, Any]) -> str:
        """Classify market phase based on indicators."""
        # Simplified logic for educational purposes
        price_bias = indicators["price_characteristics"]["directional_bias"]
        volume_quality = indicators["volume_patterns"]["volume_quality"]
        
        if price_bias == "neutral" and volume_quality == "moderate":
            return MarketPhase.RANGE.value
        elif price_bias in ["bullish", "bearish"] and volume_quality == "strong":
            return MarketPhase.TREND_UP.value if price_bias == "bullish" else MarketPhase.TREND_DOWN.value
        else:
            return MarketPhase.UNCERTAIN.value
    
    def _assess_phase_confidence(self, indicators: Dict[str, Any]) -> str:
        """Assess confidence in phase classification."""
        return "moderate"  # Educational placeholder
    
    def _get_phase_characteristics(self, phase: str) -> Dict[str, Any]:
        """Get characteristics for a market phase."""
        characteristics = {
            MarketPhase.RANGE.value: {
                "description": "Price moves within defined boundaries",
                "typical_duration": "weeks to months",
                "volatility_tendency": "moderate",
                "breakout_potential": "present"
            },
            MarketPhase.TREND_UP.value: {
                "description": "Sustained upward price movement",
                "typical_duration": "months",
                "volatility_tendency": "low_to_moderate",
                "momentum_characteristics": "positive"
            },
            MarketPhase.TREND_DOWN.value: {
                "description": "Sustained downward price movement",
                "typical_duration": "months",
                "volatility_tendency": "moderate_to_high",
                "momentum_characteristics": "negative"
            },
            MarketPhase.TRANSITION.value: {
                "description": "Market structure changing between phases",
                "typical_duration": "days to weeks",
                "volatility_tendency": "increasing",
                "uncertainty_level": "high"
            },
            MarketPhase.UNCERTAIN.value: {
                "description": "Clear phase classification not possible",
                "typical_duration": "variable",
                "volatility_tendency": "variable",
                "clarity_level": "low"
            }
        }
        
        return characteristics.get(phase, characteristics[MarketPhase.UNCERTAIN.value])
    
    def _identify_transition_risks(self, phase: str, indicators: Dict[str, Any]) -> List[str]:
        """Identify transition risks for current phase."""
        risks = [
            "Phase transitions can occur without warning",
            "Volatility often increases during transitions",
            "Liquidity may deteriorate during structural changes"
        ]
        
        if phase == MarketPhase.RANGE.value:
            risks.append("Range breakouts can be explosive and unpredictable")
        elif phase in [MarketPhase.TREND_UP.value, MarketPhase.TREND_DOWN.value]:
            risks.append("Trend exhaustion can lead to rapid reversals")
        
        return risks
    
    def _classify_volatility_regime(self, indicators: Dict[str, Any]) -> str:
        """Classify volatility regime based on indicators."""
        volatility_level = indicators["volatility_level"]["current_regime"]
        return volatility_level
    
    def _assess_regime_stability(self, indicators: Dict[str, Any]) -> str:
        """Assess stability of volatility regime."""
        persistence = indicators["volatility_persistence"]["regime_stability"]
        return persistence
    
    def _get_regime_characteristics(self, regime: str) -> Dict[str, Any]:
        """Get characteristics for volatility regime."""
        characteristics = {
            VolatilityRegime.LOW.value: {
                "description": "Minimal price fluctuations",
                "risk_profile": "lower",
                "participant_impact": "favors position holders"
            },
            VolatilityRegime.MEDIUM.value: {
                "description": "Moderate price fluctuations",
                "risk_profile": "moderate",
                "participant_impact": "balanced across strategies"
            },
            VolatilityRegime.HIGH.value: {
                "description": "Significant price fluctuations",
                "risk_profile": "higher",
                "participant_impact": "favors short-term traders"
            },
            VolatilityRegime.EXTREME.value: {
                "description": "Very large price fluctuations",
                "risk_profile": "very_high",
                "participant_impact": "creates both risks and opportunities"
            }
        }
        
        return characteristics.get(regime, characteristics[VolatilityRegime.MEDIUM.value])
    
    def _assess_volatility_risks(self, regime: str, indicators: Dict[str, Any]) -> List[str]:
        """Assess volatility-related risks."""
        risks = [
            "Volatility can increase suddenly and unexpectedly",
            "High volatility increases execution risk and slippage",
            "Volatility clustering can create extended periods of risk"
        ]
        
        if regime in [VolatilityRegime.HIGH.value, VolatilityRegime.EXTREME.value]:
            risks.append("Current regime presents elevated risk levels")
        
        return risks
    
    def _classify_liquidity_condition(self, indicators: Dict[str, Any]) -> str:
        """Classify liquidity condition based on indicators."""
        depth_level = indicators["order_book_depth"]["depth_level"]
        impact_level = indicators["market_impact"]["impact_level"]
        
        if depth_level == "high" and impact_level == "low":
            return LiquidityCondition.AMPLE.value
        elif depth_level == "low" and impact_level == "high":
            return LiquidityCondition.TIGHT.value
        else:
            return LiquidityCondition.MODERATE.value
    
    def _assess_liquidity_stability(self, indicators: Dict[str, Any]) -> str:
        """Assess stability of liquidity conditions."""
        return "moderate"  # Educational placeholder
    
    def _get_liquidity_characteristics(self, condition: str) -> Dict[str, Any]:
        """Get characteristics for liquidity condition."""
        characteristics = {
            LiquidityCondition.AMPLE.value: {
                "description": "Abundant liquidity across price levels",
                "execution_impact": "minimal",
                "cost_implications": "lower transaction costs"
            },
            LiquidityCondition.MODERATE.value: {
                "description": "Sufficient liquidity with some limitations",
                "execution_impact": "moderate",
                "cost_implications": "reasonable transaction costs"
            },
            LiquidityCondition.TIGHT.value: {
                "description": "Limited liquidity at key price levels",
                "execution_impact": "significant",
                "cost_implications": "higher transaction costs"
            },
            LiquidityCondition.VERY_TIGHT.value: {
                "description": "Very limited liquidity throughout order book",
                "execution_impact": "severe",
                "cost_implications": "very high transaction costs"
            }
        }
        
        return characteristics.get(condition, characteristics[LiquidityCondition.MODERATE.value])
    
    def _assess_execution_considerations(self, condition: str, indicators: Dict[str, Any]) -> List[str]:
        """Assess execution considerations for liquidity condition."""
        considerations = [
            "Market impact increases with trade size",
            "Timing of execution affects transaction costs",
            "Order type selection becomes more important in tight conditions"
        ]
        
        if condition in [LiquidityCondition.TIGHT.value, LiquidityCondition.VERY_TIGHT.value]:
            considerations.append("Current liquidity conditions require careful execution planning")
        
        return considerations
    
    def _assess_efficiency_level(self, indicators: Dict[str, Any]) -> str:
        """Assess overall market efficiency level."""
        # Simplified assessment for educational purposes
        return "moderate"
    
    def _identify_structural_biases(self, indicators: Dict[str, Any]) -> List[str]:
        """Identify structural market biases."""
        biases = []
        
        structural = indicators["structural_biases"]
        if structural["seasonal_patterns"] == "present":
            biases.append("Seasonal patterns suggest recurring time-based effects")
        
        if structural["day_of_week_effects"] == "present":
            biases.append("Day-of-week effects indicate weekday-based patterns")
        
        return biases
    
    def _get_efficiency_characteristics(self, level: str) -> Dict[str, Any]:
        """Get characteristics for efficiency level."""
        characteristics = {
            "high": {
                "description": "Prices quickly reflect available information",
                "arbitrage_opportunities": "rare",
                "predictability": "low"
            },
            "moderate": {
                "description": "Prices reasonably reflect available information",
                "arbitrage_opportunities": "occasional",
                "predictability": "moderate"
            },
            "low": {
                "description": "Prices may not fully reflect available information",
                "arbitrage_opportunities": "more common",
                "predictability": "higher"
            }
        }
        
        return characteristics.get(level, characteristics["moderate"])
    
    def _assess_bias_implications(self, biases: List[str]) -> List[str]:
        """Assess implications of structural biases."""
        implications = [
            "Structural biases may create temporary inefficiencies",
            "Bias exploitation requires careful risk management",
            "Biases can change or disappear over time"
        ]
        
        if biases:
            implications.append("Identified biases warrant further investigation")
        
        return implications
    
    def _assess_structure_quality(self, components: Dict[str, Any]) -> str:
        """Assess overall market structure quality."""
        # Simplified assessment for educational purposes
        return "moderate"
    
    def _assess_structure_risk_context(self, components: Dict[str, Any]) -> Dict[str, Any]:
        """Assess risk context of market structure."""
        return {
            "overall_risk": "moderate",
            "key_risk_factors": [
                "Market structure can change without warning",
                "Current conditions may not persist",
                "Structural analysis has inherent limitations"
            ]
        }
    
    def _identify_structure_strengths(self, components: Dict[str, Any]) -> List[str]:
        """Identify structural strengths."""
        strengths = []
        
        if components["liquidity_condition"] == LiquidityCondition.AMPLE.value:
            strengths.append("Strong liquidity supports efficient execution")
        
        if components["volatility_regime"] == VolatilityRegime.LOW.value:
            strengths.append("Low volatility reduces execution uncertainty")
        
        return strengths
    
    def _identify_structure_concerns(self, components: Dict[str, Any]) -> List[str]:
        """Identify structural concerns."""
        concerns = []
        
        if components["liquidity_condition"] in [LiquidityCondition.TIGHT.value, LiquidityCondition.VERY_TIGHT.value]:
            concerns.append("Tight liquidity may increase execution costs")
        
        if components["volatility_regime"] in [VolatilityRegime.HIGH.value, VolatilityRegime.EXTREME.value]:
            concerns.append("High volatility increases market risk")
        
        return concerns
    
    def _assess_market_maturity(self, components: Dict[str, Any]) -> str:
        """Assess market maturity based on structure."""
        return "developing"  # Educational placeholder
    
    def _get_educational_context(self) -> List[str]:
        """Get educational context about market structure analysis."""
        return [
            "Market structure analysis provides context for price movements",
            "Understanding structure helps assess risk and opportunity",
            "Structure analysis complements other forms of market analysis",
            "Market structure is dynamic and can change rapidly",
            "Structural analysis is educational, not predictive"
        ]
    
    def _get_assumptions(self) -> List[str]:
        """Get assumptions for market structure analysis."""
        return [
            "Market structure analysis is based on conceptual frameworks",
            "Current conditions may not reflect future states",
            "Structural patterns have varying degrees of reliability",
            "Analysis does not account for unexpected market events"
        ]
    
    def _get_limitations(self) -> List[str]:
        """Get limitations for market structure analysis."""
        return [
            "Analysis does not use real-time market data",
            "Structural analysis cannot predict market movements",
            "Market structure classification has inherent uncertainty",
            "Educational focus limits practical trading applications"
        ]
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    
    def _error_response(self, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "error": True,
            "message": f"Market structure analysis failed: {error_message}",
            "educational_context": self._get_educational_context(),
            "assumptions": self._get_assumptions(),
            "limitations": self._get_limitations()
        }
