"""
Deep Research Pipeline for MacroChain AI.

This module implements a structured, deterministic research pipeline that
orchestrates comprehensive crypto market analysis across multiple dimensions.
"""

from typing import Dict, Any, List, Optional
import logging
from dataclasses import dataclass
from enum import Enum
from .macro import MacroAnalyzer
from .sentiment import SentimentAnalyzer
from .onchain import OnChainAnalyzer
from .market_structure import MarketStructureAnalyzer


logger = logging.getLogger(__name__)


class ResearchPhase(Enum):
    """Research pipeline phases."""
    MACRO = "macro"
    SENTIMENT = "sentiment"
    ONCHAIN = "onchain"
    MARKET_STRUCTURE = "market_structure"
    SYNTHESIS = "synthesis"


@dataclass
class ResearchContext:
    """Context for research pipeline execution."""
    query: str
    assets: List[str]
    timestamp: str
    research_id: str
    assumptions: List[str]
    limitations: List[str]


@dataclass
class PhaseResult:
    """Result from a research pipeline phase."""
    phase: ResearchPhase
    data: Dict[str, Any]
    confidence: str
    assumptions: List[str]
    limitations: List[str]
    execution_time: float


class ResearchPipeline:
    """
    Structured research pipeline for comprehensive crypto market analysis.
    
    This class implements a deterministic, repeatable research process that
    systematically analyzes markets across multiple dimensions while maintaining
    strict educational focus and risk awareness.
    """
    
    def __init__(self):
        """Initialize the research pipeline."""
        self.macro_analyzer = MacroAnalyzer()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.onchain_analyzer = OnChainAnalyzer()
        self.market_structure_analyzer = MarketStructureAnalyzer()
        
        self.pipeline_phases = [
            ResearchPhase.MACRO,
            ResearchPhase.SENTIMENT,
            ResearchPhase.ONCHAIN,
            ResearchPhase.MARKET_STRUCTURE,
            ResearchPhase.SYNTHESIS
        ]
    
    def execute_research(
        self, 
        query: str, 
        assets: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Execute the complete research pipeline.
        
        Args:
            query: Research query to analyze
            assets: List of assets to focus on (optional)
            
        Returns:
            Complete research results with all phases
        """
        try:
            import time
            import uuid
            from datetime import datetime
            
            logger.info(f"Starting research pipeline for query: {query}")
            
            # Initialize research context
            context = ResearchContext(
                query=query,
                assets=assets or ["bitcoin", "ethereum"],
                timestamp=datetime.utcnow().isoformat() + "Z",
                research_id=str(uuid.uuid4()),
                assumptions=[],
                limitations=[]
            )
            
            # Execute pipeline phases
            phase_results = []
            total_start_time = time.time()
            
            for phase in self.pipeline_phases:
                if phase == ResearchPhase.SYNTHESIS:
                    result = self._execute_synthesis_phase(context, phase_results)
                else:
                    result = self._execute_analysis_phase(phase, context)
                
                phase_results.append(result)
                logger.info(f"Completed phase: {phase.value}")
            
            total_execution_time = time.time() - total_start_time
            
            # Compile final research report
            research_report = self._compile_research_report(
                context, phase_results, total_execution_time
            )
            
            logger.info(f"Research pipeline completed in {total_execution_time:.2f}s")
            return research_report
            
        except Exception as e:
            logger.error(f"Research pipeline failed: {str(e)}")
            return self._error_response(context, str(e))
    
    def _execute_analysis_phase(
        self, 
        phase: ResearchPhase, 
        context: ResearchContext
    ) -> PhaseResult:
        """
        Execute a single analysis phase.
        
        Args:
            phase: Research phase to execute
            context: Research context
            
        Returns:
            Phase execution result
        """
        import time
        start_time = time.time()
        
        try:
            if phase == ResearchPhase.MACRO:
                data = self.macro_analyzer.analyze(context.query, context.assets)
            elif phase == ResearchPhase.SENTIMENT:
                data = self.sentiment_analyzer.analyze(context.query, context.assets)
            elif phase == ResearchPhase.ONCHAIN:
                data = self.onchain_analyzer.analyze(context.query, context.assets)
            elif phase == ResearchPhase.MARKET_STRUCTURE:
                data = self.market_structure_analyzer.analyze(context.query, context.assets)
            else:
                raise ValueError(f"Unknown analysis phase: {phase}")
            
            execution_time = time.time() - start_time
            
            return PhaseResult(
                phase=phase,
                data=data,
                confidence=data.get("confidence_level", "moderate"),
                assumptions=data.get("assumptions", []),
                limitations=data.get("limitations", []),
                execution_time=execution_time
            )
            
        except Exception as e:
            logger.error(f"Phase {phase.value} failed: {str(e)}")
            return PhaseResult(
                phase=phase,
                data={"error": str(e)},
                confidence="low",
                assumptions=[f"Analysis failed: {str(e)}"],
                limitations=["Phase execution error"],
                execution_time=time.time() - start_time
            )
    
    def _execute_synthesis_phase(
        self, 
        context: ResearchContext, 
        phase_results: List[PhaseResult]
    ) -> PhaseResult:
        """
        Execute synthesis phase to combine all analyses.
        
        Args:
            context: Research context
            phase_results: Results from previous phases
            
        Returns:
            Synthesis phase result
        """
        import time
        start_time = time.time()
        
        try:
            # Extract data from previous phases
            macro_data = self._get_phase_data(phase_results, ResearchPhase.MACRO)
            sentiment_data = self._get_phase_data(phase_results, ResearchPhase.SENTIMENT)
            onchain_data = self._get_phase_data(phase_results, ResearchPhase.ONCHAIN)
            structure_data = self._get_phase_data(phase_results, ResearchPhase.MARKET_STRUCTURE)
            
            # Perform synthesis
            synthesis_data = self._synthesize_analyses(
                macro_data, sentiment_data, onchain_data, structure_data, context
            )
            
            execution_time = time.time() - start_time
            
            return PhaseResult(
                phase=ResearchPhase.SYNTHESIS,
                data=synthesis_data,
                confidence=synthesis_data.get("confidence_level", "moderate"),
                assumptions=synthesis_data.get("assumptions", []),
                limitations=synthesis_data.get("limitations", []),
                execution_time=execution_time
            )
            
        except Exception as e:
            logger.error(f"Synthesis phase failed: {str(e)}")
            return PhaseResult(
                phase=ResearchPhase.SYNTHESIS,
                data={"error": str(e)},
                confidence="low",
                assumptions=[f"Synthesis failed: {str(e)}"],
                limitations=["Synthesis execution error"],
                execution_time=time.time() - start_time
            )
    
    def _get_phase_data(self, phase_results: List[PhaseResult], phase: ResearchPhase) -> Dict[str, Any]:
        """Get data from a specific phase result."""
        for result in phase_results:
            if result.phase == phase:
                return result.data
        return {}
    
    def _synthesize_analyses(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any],
        context: ResearchContext
    ) -> Dict[str, Any]:
        """
        Synthesize analyses from all phases into unified insights.
        
        Args:
            macro: Macro analysis data
            sentiment: Sentiment analysis data
            onchain: On-chain analysis data
            structure: Market structure analysis data
            context: Research context
            
        Returns:
            Synthesized analysis data
        """
        # Collect all insights
        all_insights = []
        
        # Extract insights from each phase
        if macro and not macro.get("error"):
            all_insights.extend(macro.get("insights", []))
        
        if sentiment and not sentiment.get("error"):
            all_insights.extend(sentiment.get("insights", []))
        
        if onchain and not onchain.get("error"):
            all_insights.extend(onchain.get("insights", []))
        
        if structure and not structure.get("error"):
            all_insights.extend(structure.get("insights", []))
        
        # Identify cross-phase correlations
        correlations = self._identify_cross_phase_correlations(
            macro, sentiment, onchain, structure
        )
        
        # Assess overall market state
        market_state = self._assess_overall_market_state(
            macro, sentiment, onchain, structure
        )
        
        # Compile assumptions and limitations
        assumptions = self._compile_assumptions(macro, sentiment, onchain, structure)
        limitations = self._compile_limitations(macro, sentiment, onchain, structure)
        
        return {
            "synthesis_type": "comprehensive_market_analysis",
            "total_insights": len(all_insights),
            "key_insights": all_insights[:10],  # Top 10 insights
            "cross_phase_correlations": correlations,
            "overall_market_state": market_state,
            "research_quality": self._assess_research_quality(macro, sentiment, onchain, structure),
            "assumptions": assumptions,
            "limitations": limitations,
            "confidence_level": self._calculate_overall_confidence(macro, sentiment, onchain, structure)
        }
    
    def _identify_cross_phase_correlations(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Identify correlations across different analysis phases."""
        correlations = []
        
        # Macro-Sentiment correlations
        if (macro.get("overall_conditions", {}).get("overall") == "challenging" and
            sentiment.get("overall_sentiment", {}).get("overall_sentiment") == "negative"):
            correlations.append({
                "type": "macro_sentiment",
                "phases": ["macro", "sentiment"],
                "observation": "Challenging macro conditions align with negative sentiment",
                "strength": "strong",
                "significance": "high"
            })
        
        # On-Chain-Structure correlations
        if (onchain.get("network_conditions", {}).get("overall_status") == "positive" and
            structure.get("market_phase", {}).get("trend_strength") == "strong"):
            correlations.append({
                "type": "onchain_structure",
                "phases": ["onchain", "market_structure"],
                "observation": "Strong network fundamentals support robust market structure",
                "strength": "moderate",
                "significance": "medium"
            })
        
        # Sentiment-Structure correlations
        if (sentiment.get("overall_sentiment", {}).get("overall_sentiment") == "neutral" and
            structure.get("market_phase", {}).get("phase") == "range"):
            correlations.append({
                "type": "sentiment_structure",
                "phases": ["sentiment", "market_structure"],
                "observation": "Neutral sentiment coincides with range-bound market structure",
                "strength": "moderate",
                "significance": "medium"
            })
        
        return correlations
    
    def _assess_overall_market_state(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assess overall market state from all phases."""
        state_indicators = {}
        
        # Collect state indicators
        if macro:
            state_indicators["macro"] = macro.get("overall_conditions", {}).get("overall", "neutral")
        
        if sentiment:
            state_indicators["sentiment"] = sentiment.get("overall_sentiment", {}).get("overall_sentiment", "neutral")
        
        if onchain:
            state_indicators["onchain"] = onchain.get("network_conditions", {}).get("overall_status", "neutral")
        
        if structure:
            state_indicators["structure"] = structure.get("market_phase", {}).get("overall_bias", "neutral")
        
        # Determine overall state
        positive_count = sum(1 for v in state_indicators.values() if v in ["positive", "supportive", "strong"])
        negative_count = sum(1 for v in state_indicators.values() if v in ["negative", "challenging", "weak"])
        
        if positive_count > negative_count:
            overall_state = "positive"
        elif negative_count > positive_count:
            overall_state = "negative"
        else:
            overall_state = "neutral"
        
        return {
            "overall_state": overall_state,
            "phase_indicators": state_indicators,
            "state_confidence": "moderate",
            "dominant_factors": self._identify_dominant_factors(state_indicators)
        }
    
    def _identify_dominant_factors(self, state_indicators: Dict[str, str]) -> List[str]:
        """Identify dominant factors in market state assessment."""
        dominant = []
        
        for phase, state in state_indicators.items():
            if state not in ["neutral"]:
                dominant.append(f"{phase.title()}: {state}")
        
        return dominant
    
    def _compile_assumptions(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[str]:
        """Compile assumptions from all phases."""
        assumptions = [
            "Analysis is based on conceptual and educational frameworks",
            "Market conditions are dynamic and may change rapidly",
            "Historical patterns may not repeat in future conditions",
            "Multiple factors influence cryptocurrency market dynamics"
        ]
        
        # Add phase-specific assumptions
        for phase_name, phase_data in [("macro", macro), ("sentiment", sentiment), 
                                     ("onchain", onchain), ("structure", structure)]:
            if phase_data and not phase_data.get("error"):
                phase_assumptions = phase_data.get("assumptions", [])
                for assumption in phase_assumptions:
                    assumptions.append(f"{phase_name.title()}: {assumption}")
        
        return assumptions
    
    def _compile_limitations(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> List[str]:
        """Compile limitations from all phases."""
        limitations = [
            "Analysis does not use real-time market data",
            "Educational focus limits predictive capabilities",
            "Market complexity exceeds analytical frameworks",
            "Unforeseen events can invalidate current analysis"
        ]
        
        # Add phase-specific limitations
        for phase_name, phase_data in [("macro", macro), ("sentiment", sentiment), 
                                     ("onchain", onchain), ("structure", structure)]:
            if phase_data and not phase_data.get("error"):
                phase_limitations = phase_data.get("limitations", [])
                for limitation in phase_limitations:
                    limitations.append(f"{phase_name.title()}: {limitation}")
        
        return limitations
    
    def _assess_research_quality(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assess overall research quality."""
        successful_phases = sum(1 for data in [macro, sentiment, onchain, structure] 
                              if data and not data.get("error"))
        
        total_phases = 4
        
        quality_score = successful_phases / total_phases
        
        if quality_score >= 0.75:
            quality_level = "high"
        elif quality_score >= 0.5:
            quality_level = "moderate"
        else:
            quality_level = "low"
        
        return {
            "quality_level": quality_level,
            "successful_phases": successful_phases,
            "total_phases": total_phases,
            "quality_score": quality_score,
            "completeness": f"{successful_phases}/{total_phases} phases completed"
        }
    
    def _calculate_overall_confidence(
        self,
        macro: Dict[str, Any],
        sentiment: Dict[str, Any],
        onchain: Dict[str, Any],
        structure: Dict[str, Any]
    ) -> str:
        """Calculate overall confidence in research results."""
        confidences = []
        
        for data in [macro, sentiment, onchain, structure]:
            if data and not data.get("error"):
                conf = data.get("confidence_level", "moderate")
                confidences.append(conf)
        
        if not confidences:
            return "low"
        
        # Map confidence levels to scores
        confidence_scores = {"high": 3, "moderate": 2, "low": 1}
        scores = [confidence_scores.get(conf, 2) for conf in confidences]
        
        avg_score = sum(scores) / len(scores)
        
        if avg_score >= 2.5:
            return "moderate_to_high"
        elif avg_score >= 1.5:
            return "moderate"
        else:
            return "low"
    
    def _compile_research_report(
        self,
        context: ResearchContext,
        phase_results: List[PhaseResult],
        total_execution_time: float
    ) -> Dict[str, Any]:
        """Compile final research report."""
        # Extract synthesis data
        synthesis_result = None
        for result in phase_results:
            if result.phase == ResearchPhase.SYNTHESIS:
                synthesis_result = result
                break
        
        synthesis_data = synthesis_result.data if synthesis_result else {}
        
        return {
            "research_metadata": {
                "research_id": context.research_id,
                "query": context.query,
                "assets_analyzed": context.assets,
                "timestamp": context.timestamp,
                "total_execution_time": total_execution_time,
                "pipeline_version": "1.0.0"
            },
            "pipeline_execution": {
                "phases_completed": len([r for r in phase_results if not r.data.get("error")]),
                "total_phases": len(self.pipeline_phases),
                "phase_details": {
                    result.phase.value: {
                        "execution_time": result.execution_time,
                        "confidence": result.confidence,
                        "status": "success" if not result.data.get("error") else "failed"
                    }
                    for result in phase_results
                }
            },
            "research_findings": synthesis_data,
            "phase_results": {
                result.phase.value: result.data
                for result in phase_results
                if result.phase != ResearchPhase.SYNTHESIS
            },
            "research_quality": synthesis_data.get("research_quality", {}),
            "assumptions": synthesis_data.get("assumptions", []),
            "limitations": synthesis_data.get("limitations", []),
            "disclaimer": self._get_research_disclaimer()
        }
    
    def _get_research_disclaimer(self) -> str:
        """Get research disclaimer."""
        return (
            "This research report is for educational and informational purposes only. "
            "It does not constitute financial advice, investment recommendations, or trading signals. "
            "Cryptocurrency markets are highly volatile and risky. Always conduct your own research "
            "and consult with qualified financial professionals before making any investment decisions."
        )
    
    def _error_response(self, context: ResearchContext, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "research_metadata": {
                "research_id": context.research_id,
                "query": context.query,
                "assets_analyzed": context.assets,
                "timestamp": context.timestamp,
                "pipeline_version": "1.0.0"
            },
            "error": True,
            "message": f"Research pipeline failed: {error_message}",
            "disclaimer": self._get_research_disclaimer()
        }
