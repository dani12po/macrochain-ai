"""
Professional Research Report Formatter for MacroChain AI.

This module formats analysis results into professional crypto market research
reports with competition-grade structure and presentation.
"""

from typing import Dict, Any, List
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


class ResearchFormatter:
    """
    Formats analysis results into professional research reports.
    
    This class creates competition-grade crypto market research reports
    with proper structure, professional language, and clear risk disclaimers.
    """
    
    def __init__(self):
        """Initialize the research formatter."""
        self.report_sections = [
            "header",
            "research_focus",
            "macro_context",
            "market_sentiment",
            "onchain_overview", 
            "market_structure",
            "key_insights",
            "risks_uncertainty",
            "disclaimer"
        ]
    
    def format_research_report(
        self, 
        analysis_data: Dict[str, Any],
        user_query: str
    ) -> Dict[str, Any]:
        """
        Format complete research report.
        
        Args:
            analysis_data: Raw analysis data from research pipeline
            user_query: Original user query
            
        Returns:
            Formatted research report dictionary
        """
        try:
            logger.info("Formatting professional research report")
            
            formatted_report = {
                "report_header": self._format_report_header(analysis_data, user_query),
                "research_focus": self._format_research_focus(user_query, analysis_data),
                "macro_context": self._format_macro_context(analysis_data),
                "market_sentiment": self._format_market_sentiment(analysis_data),
                "onchain_overview": self._format_onchain_overview(analysis_data),
                "market_structure": self._format_market_structure(analysis_data),
                "key_insights": self._format_key_insights(analysis_data),
                "risks_uncertainty": self._format_risks_uncertainty(analysis_data),
                "disclaimer": self._get_professional_disclaimer(),
                "report_metadata": self._format_report_metadata(analysis_data)
            }
            
            logger.info("Research report formatting completed")
            return formatted_report
            
        except Exception as e:
            logger.error(f"Error formatting research report: {str(e)}")
            return self._error_response(user_query, str(e))
    
    def _format_report_header(self, analysis_data: Dict[str, Any], query: str) -> Dict[str, Any]:
        """
        Format professional report header.
        
        Args:
            analysis_data: Complete analysis data
            query: User query
            
        Returns:
            Formatted report header
        """
        timestamp = analysis_data.get("research_metadata", {}).get("timestamp", self._get_timestamp())
        assets = analysis_data.get("research_metadata", {}).get("assets_analyzed", [])
        
        return {
            "title": "MACROCHAIN — CRYPTO MARKET RESEARCH REPORT",
            "subtitle": f"Analysis of {', '.join(assets).title()} Markets",
            "research_query": query,
            "publication_date": timestamp,
            "report_id": analysis_data.get("research_metadata", {}).get("research_id", "UNKNOWN"),
            "version": "1.0",
            "classification": "EDUCATIONAL RESEARCH"
        }
    
    def _format_research_focus(self, query: str, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format research focus section.
        
        Args:
            query: User query
            analysis_data: Analysis data
            
        Returns:
            Formatted research focus
        """
        assets = analysis_data.get("research_metadata", {}).get("assets_analyzed", [])
        
        focus_description = f"Comprehensive analysis of {', '.join(assets).title()} market dynamics based on query: '{query}'"
        
        methodology = [
            "Multi-dimensional market analysis framework",
            "Macroeconomic context assessment",
            "Market sentiment and psychology evaluation", 
            "On-chain metrics analysis",
            "Market structure and risk context examination",
            "Cross-correlation synthesis"
        ]
        
        return {
            "research_objective": focus_description,
            "methodology": methodology,
            "scope": f"Analysis covers {', '.join(assets).title()} with focus on educational market understanding",
            "analytical_framework": "Structured research pipeline with deterministic methodology",
            "time_horizon": "Current market conditions with educational context"
        }
    
    def _format_macro_context(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format macro context section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted macro context
        """
        macro_data = analysis_data.get("phase_results", {}).get("macro", {})
        
        if macro_data.get("error"):
            return self._format_section_error("Macroeconomic Analysis")
        
        # Extract key macro information
        overall_conditions = macro_data.get("overall_conditions", {})
        liquidity_conditions = macro_data.get("liquidity_conditions", {})
        rate_environment = macro_data.get("interest_rate_environment", {})
        
        context_points = []
        
        # Liquidity context
        if liquidity_conditions.get("overall_status"):
            context_points.append(f"Global liquidity conditions appear {liquidity_conditions['overall_status']}")
        
        # Rate environment context
        if rate_environment.get("implications", {}).get("overall"):
            context_points.append(f"Interest rate environment presents {rate_environment['implications']['overall']} implications")
        
        # Overall conditions
        if overall_conditions.get("overall"):
            context_points.append(f"Overall macroeconomic conditions assessed as {overall_conditions['overall']}")
        
        # Add key factors
        key_factors = overall_conditions.get("key_factors", [])
        if key_factors:
            context_points.extend([f"Key factor: {factor}" for factor in key_factors[:3]])
        
        return {
            "section_title": "MACRO CONTEXT",
            "overall_assessment": overall_conditions.get("overall", "neutral"),
            "key_observations": context_points,
            "liquidity_analysis": {
                "status": liquidity_conditions.get("overall_status", "moderate"),
                "trend": liquidity_conditions.get("trend", "stable"),
                "key_considerations": liquidity_conditions.get("key_observations", [])
            },
            "monetary_policy_context": {
                "implications": rate_environment.get("implications", {}).get("overall", "neutral"),
                "trend": rate_environment.get("trend", "monitoring"),
                "key_considerations": rate_environment.get("educational_context", [])
            },
            "risk_considerations": macro_data.get("educational_notes", []),
            "confidence_level": macro_data.get("confidence_level", "moderate")
        }
    
    def _format_market_sentiment(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format market sentiment section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted market sentiment
        """
        sentiment_data = analysis_data.get("phase_results", {}).get("sentiment", {})
        
        if sentiment_data.get("error"):
            return self._format_section_error("Market Sentiment Analysis")
        
        overall_sentiment = sentiment_data.get("overall_sentiment", {})
        fear_greed = sentiment_data.get("fear_greed_index", {})
        social_sentiment = sentiment_data.get("social_media_sentiment", {})
        
        sentiment_points = []
        
        # Overall sentiment
        if overall_sentiment.get("overall_sentiment"):
            sentiment_points.append(f"Overall market sentiment assessed as {overall_sentiment['overall_sentiment']}")
        
        # Fear & Greed context
        if fear_greed.get("sentiment_level"):
            sentiment_points.append(f"Fear & Greed indicators show {fear_greed['sentiment_level']} sentiment")
        
        # Social media context
        if social_sentiment.get("overall_social_sentiment"):
            sentiment_points.append(f"Social media sentiment appears {social_sentiment['overall_social_sentiment']}")
        
        # Key drivers
        key_drivers = overall_sentiment.get("key_drivers", [])
        if key_drivers:
            sentiment_points.extend([f"Driver: {driver}" for driver in key_drivers[:3]])
        
        return {
            "section_title": "MARKET SENTIMENT",
            "overall_assessment": overall_sentiment.get("overall_sentiment", "neutral"),
            "sentiment_indicators": {
                "fear_greed_index": {
                    "level": fear_greed.get("sentiment_level", "neutral"),
                    "interpretation": fear_greed.get("educational_notes", [])[:2]
                },
                "social_media": {
                    "overall": social_sentiment.get("overall_social_sentiment", "neutral"),
                    "volume_trends": social_sentiment.get("volume_trends", "stable")
                },
                "news_sentiment": sentiment_data.get("news_sentiment", {}).get("media_bias_analysis", {})
            },
            "psychological_factors": sentiment_points,
            "contrarian_signals": overall_sentiment.get("contrarian_signals", []),
            "confidence_level": overall_sentiment.get("confidence", "moderate")
        }
    
    def _format_onchain_overview(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format on-chain overview section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted on-chain overview
        """
        onchain_data = analysis_data.get("phase_results", {}).get("onchain", {})
        
        if onchain_data.get("error"):
            return self._format_section_error("On-Chain Analysis")
        
        network_conditions = onchain_data.get("network_conditions", {})
        activity_metrics = onchain_data.get("network_activity", {})
        holder_metrics = onchain_data.get("holder_behavior", {})
        
        onchain_points = []
        
        # Overall network health
        if network_conditions.get("overall_status"):
            onchain_points.append(f"Network health assessed as {network_conditions['overall_status']}")
        
        # Activity trends
        if activity_metrics.get("overall_activity", {}).get("trend"):
            onchain_points.append(f"Network activity shows {activity_metrics['overall_activity']['trend']} trend")
        
        # Holder behavior
        if holder_metrics.get("behavioral_insights", {}).get("long_term_trend"):
            onchain_points.append(f"Long-term holder behavior indicates {holder_metrics['behavioral_insights']['long_term_trend']}")
        
        # Key strengths and concerns
        strengths = network_conditions.get("strengths", [])
        concerns = network_conditions.get("concerns", [])
        
        if strengths:
            onchain_points.extend([f"Strength: {strength}" for strength in strengths[:2]])
        
        if concerns:
            onchain_points.extend([f"Concern: {concern}" for concern in concerns[:2]])
        
        return {
            "section_title": "ON-CHAIN OVERVIEW",
            "network_health": network_conditions.get("overall_status", "moderate"),
            "activity_trends": {
                "overall_trend": activity_metrics.get("overall_activity", {}).get("trend", "stable"),
                "growth_indicators": activity_metrics.get("growth_indicators", []),
                "usage_patterns": activity_metrics.get("usage_patterns", {})
            },
            "holder_dynamics": {
                "distribution_trends": holder_metrics.get("behavioral_insights", {}),
                "market_maturity": holder_metrics.get("market_maturity", "developing"),
                "risk_indicators": holder_metrics.get("risk_indicators", [])
            },
            "fundamental_indicators": onchain_points,
            "network_efficiency": onchain_data.get("transaction_metrics", {}).get("efficiency_metrics", {}),
            "confidence_level": network_conditions.get("confidence_level", "moderate")
        }
    
    def _format_market_structure(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format market structure section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted market structure
        """
        structure_data = analysis_data.get("phase_results", {}).get("market_structure", {})
        
        if structure_data.get("error"):
            return self._format_section_error("Market Structure Analysis")
        
        structure_assessment = structure_data.get("structure_assessment", {})
        market_phase = structure_data.get("market_phase", {})
        volatility_regime = structure_data.get("volatility_regime", {})
        liquidity_conditions = structure_data.get("liquidity_conditions", {})
        
        structure_points = []
        
        # Overall structure
        if structure_assessment.get("structure_quality"):
            structure_points.append(f"Market structure quality assessed as {structure_assessment['structure_quality']}")
        
        # Market phase
        if market_phase.get("current_phase"):
            structure_points.append(f"Current market phase identified as {market_phase['current_phase']}")
        
        # Volatility regime
        if volatility_regime.get("current_regime"):
            structure_points.append(f"Volatility regime classified as {volatility_regime['current_regime']}")
        
        # Liquidity conditions
        if liquidity_conditions.get("current_condition"):
            structure_points.append(f"Liquidity conditions are {liquidity_conditions['current_condition']}")
        
        # Risk context
        risk_context = structure_assessment.get("risk_context", {})
        if risk_context.get("overall_risk"):
            structure_points.append(f"Overall structural risk context: {risk_context['overall_risk']}")
        
        return {
            "section_title": "MARKET STRUCTURE",
            "structure_quality": structure_assessment.get("structure_quality", "moderate"),
            "market_phase": {
                "current_phase": market_phase.get("current_phase", "uncertain"),
                "confidence": market_phase.get("phase_confidence", "moderate"),
                "characteristics": market_phase.get("phase_characteristics", {}),
                "transition_risks": market_phase.get("transition_risks", [])
            },
            "volatility_regime": {
                "current_regime": volatility_regime.get("current_regime", "medium"),
                "stability": volatility_regime.get("regime_stability", "moderate"),
                "characteristics": volatility_regime.get("regime_characteristics", {}),
                "risk_implications": volatility_regime.get("risk_implications", [])
            },
            "liquidity_analysis": {
                "condition": liquidity_conditions.get("current_condition", "moderate"),
                "stability": liquidity_conditions.get("condition_stability", "moderate"),
                "characteristics": liquidity_conditions.get("condition_characteristics", {}),
                "execution_considerations": liquidity_conditions.get("execution_considerations", [])
            },
            "structural_assessment": structure_points,
            "risk_context": risk_context,
            "confidence_level": "moderate"
        }
    
    def _format_key_insights(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format key insights section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted key insights
        """
        research_findings = analysis_data.get("research_findings", {})
        correlations = research_findings.get("cross_phase_correlations", [])
        key_insights = research_findings.get("key_insights", [])
        
        # Compile insights from different sources
        all_insights = []
        
        # Add correlation insights
        for correlation in correlations:
            if correlation.get("observation"):
                all_insights.append({
                    "type": "cross_phase_correlation",
                    "insight": correlation["observation"],
                    "strength": correlation.get("strength", "moderate"),
                    "phases": correlation.get("phases", [])
                })
        
        # Add key insights
        for insight in key_insights:
            all_insights.append({
                "type": "key_insight",
                "insight": insight,
                "strength": "moderate",
                "phases": ["synthesis"]
            })
        
        # Add market state insights
        market_state = research_findings.get("overall_market_state", {})
        if market_state.get("dominant_factors"):
            for factor in market_state["dominant_factors"]:
                all_insights.append({
                    "type": "market_state_factor",
                    "insight": factor,
                    "strength": "moderate",
                    "phases": ["synthesis"]
                })
        
        return {
            "section_title": "KEY INSIGHTS",
            "total_insights": len(all_insights),
            "insight_categories": {
                "cross_phase_correlations": len([i for i in all_insights if i["type"] == "cross_phase_correlation"]),
                "market_state_factors": len([i for i in all_insights if i["type"] == "market_state_factor"]),
                "synthesis_insights": len([i for i in all_insights if i["type"] == "key_insight"])
            },
            "insights": all_insights[:10],  # Top 10 insights
            "confidence_level": research_findings.get("confidence_level", "moderate"),
            "research_quality": research_findings.get("research_quality", {})
        }
    
    def _format_risks_uncertainty(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format risks and uncertainty section.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted risks and uncertainty
        """
        limitations = analysis_data.get("limitations", [])
        assumptions = analysis_data.get("assumptions", [])
        research_findings = analysis_data.get("research_findings", {})
        
        # Compile risk factors
        risk_factors = []
        
        # Add limitations as risk factors
        for limitation in limitations:
            risk_factors.append({
                "category": "methodological_limitation",
                "risk": limitation,
                "mitigation": "Recognize limitation in interpretation"
            })
        
        # Add assumptions as risk factors
        for assumption in assumptions:
            risk_factors.append({
                "category": "analytical_assumption",
                "risk": assumption,
                "mitigation": "Validate assumption with additional research"
            })
        
        # Add standard crypto market risks
        standard_risks = [
            "Cryptocurrency market volatility and price fluctuations",
            "Regulatory uncertainty and policy changes",
            "Technology and security risks including hacks and vulnerabilities",
            "Liquidity risks and market manipulation potential",
            "Correlation risks with traditional financial markets"
        ]
        
        for risk in standard_risks:
            risk_factors.append({
                "category": "market_risk",
                "risk": risk,
                "mitigation": "Comprehensive risk management and diversification"
            })
        
        return {
            "section_title": "KEY RISKS & UNCERTAINTY",
            "risk_categories": {
                "methodological_limitations": len([r for r in risk_factors if r["category"] == "methodological_limitation"]),
                "analytical_assumptions": len([r for r in risk_factors if r["category"] == "analytical_assumption"]),
                "market_risks": len([r for r in risk_factors if r["category"] == "market_risk"])
            },
            "risk_factors": risk_factors[:15],  # Top 15 risk factors
            "uncertainty_level": "moderate_to_high",
            "research_limitations": limitations,
            "key_assumptions": assumptions,
            "confidence_caveats": [
                "Analysis based on educational frameworks, not real-time data",
                "Market conditions can change rapidly and unpredictably",
                "Historical patterns may not repeat in future conditions",
                "Multiple factors influence cryptocurrency market dynamics"
            ]
        }
    
    def _format_report_metadata(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format report metadata.
        
        Args:
            analysis_data: Analysis data
            
        Returns:
            Formatted report metadata
        """
        research_metadata = analysis_data.get("research_metadata", {})
        pipeline_execution = analysis_data.get("pipeline_execution", {})
        research_quality = analysis_data.get("research_findings", {}).get("research_quality", {})
        
        return {
            "research_metadata": {
                "report_id": research_metadata.get("research_id", "UNKNOWN"),
                "query": research_metadata.get("query", ""),
                "assets_analyzed": research_metadata.get("assets_analyzed", []),
                "timestamp": research_metadata.get("timestamp", self._get_timestamp()),
                "execution_time_seconds": research_metadata.get("total_execution_time", 0),
                "pipeline_version": research_metadata.get("pipeline_version", "1.0.0")
            },
            "execution_summary": {
                "phases_completed": pipeline_execution.get("phases_completed", 0),
                "total_phases": pipeline_execution.get("total_phases", 0),
                "success_rate": f"{(pipeline_execution.get('phases_completed', 0) / max(pipeline_execution.get('total_phases', 1), 1)) * 100:.1f}%"
            },
            "quality_metrics": research_quality,
            "data_sources": "Educational and conceptual frameworks",
            "analytical_approach": "Structured research pipeline with deterministic methodology",
            "report_classification": "EDUCATIONAL RESEARCH - NOT FINANCIAL ADVICE"
        }
    
    def _format_section_error(self, section_name: str) -> Dict[str, Any]:
        """Format error for a specific section."""
        return {
            "section_title": section_name.upper(),
            "error": True,
            "message": f"{section_name} data unavailable",
            "status": "section_failed",
            "confidence_level": "low"
        }
    
    def _get_professional_disclaimer(self) -> str:
        """
        Get professional research disclaimer.
        
        Returns:
            Professional disclaimer string
        """
        return (
            "**DISCLAIMER**\n\n"
            "This research report is for **EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY**. "
            "It does **NOT** constitute financial advice, investment recommendations, "
            "trading signals, or price predictions.\n\n"
            "**RISK WARNING:** Cryptocurrency markets are **HIGHLY VOLATILE AND RISKY**. "
            "Prices can fluctuate dramatically, and you may lose ALL of your invested capital.\n\n"
            "**NO INVESTMENT ADVICE:** This analysis is designed to help you UNDERSTAND market dynamics, "
            "NOT to tell you when to buy, sell, or hold any cryptocurrency.\n\n"
            "**DO YOUR OWN RESEARCH:** Always conduct your own thorough research and consult with "
            "qualified financial professionals before making any investment decisions.\n\n"
            "**PAST PERFORMANCE:** Past performance does not indicate future results. "
            "Historical patterns may not repeat in current or future market conditions.\n\n"
            "**MARKET UNCERTAINTY:** Cryptocurrency markets are inherently unpredictable and "
            "subject to numerous risks including regulatory changes, technological failures, "
            "and market manipulation.\n\n"
            "By reading this report, you acknowledge that you understand these risks and "
            "agree that this information is for educational purposes only."
        )
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        return datetime.utcnow().isoformat() + "Z"
    
    def _error_response(self, query: str, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "error": True,
            "message": f"Research report formatting failed: {error_message}",
            "disclaimer": self._get_professional_disclaimer(),
            "timestamp": self._get_timestamp()
        }
