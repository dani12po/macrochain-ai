"""
On-chain analysis module for MacroChain AI.

This module handles the analysis of on-chain metrics and blockchain
activity, providing educational insights about network fundamentals
and blockchain ecosystem dynamics.
"""

from typing import Dict, Any, List
import logging


logger = logging.getLogger(__name__)


class OnChainAnalyzer:
    """
    Analyzes on-chain metrics and blockchain fundamentals.
    
    This class provides educational analysis of blockchain activity,
    network health, and on-chain indicators without providing
    investment advice or trading signals.
    """
    
    def __init__(self):
        """Initialize the on-chain analyzer."""
        self.onchain_categories = [
            "network_activity",
            "holder_behavior",
            "transaction_metrics",
            "network_health",
            "development_activity",
            "economic_metrics"
        ]
    
    def analyze(self, query: str, assets: List[str] = None) -> Dict[str, Any]:
        """
        Perform on-chain analysis based on the query.
        
        Args:
            query: User's analysis request
            assets: List of assets to focus on (optional)
            
        Returns:
            Dictionary containing on-chain analysis results
        """
        try:
            logger.info(f"Starting on-chain analysis for query: {query}")
            
            # Analyze different on-chain components
            network_activity = self._analyze_network_activity()
            holder_behavior = self._analyze_holder_behavior()
            transaction_metrics = self._analyze_transaction_metrics()
            network_health = self._analyze_network_health()
            
            # Generate insights
            insights = self._generate_onchain_insights(
                network_activity,
                holder_behavior,
                transaction_metrics,
                network_health
            )
            
            # Assess overall network conditions
            network_conditions = self._assess_network_conditions(
                network_activity,
                holder_behavior,
                transaction_metrics,
                network_health
            )
            
            result = {
                "analysis_type": "onchain",
                "network_activity": network_activity,
                "holder_behavior": holder_behavior,
                "transaction_metrics": transaction_metrics,
                "network_health": network_health,
                "network_conditions": network_conditions,
                "insights": insights,
                "educational_explanations": self._get_educational_explanations(),
                "timestamp": self._get_timestamp()
            }
            
            logger.info("On-chain analysis completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error in on-chain analysis: {str(e)}")
            return self._error_response(str(e))
    
    def _analyze_network_activity(self) -> Dict[str, Any]:
        """
        Analyze network activity metrics.
        
        Returns:
            Dictionary with network activity analysis
        """
        activity_metrics = {
            "active_addresses": {
                "current_trend": "stable",  # Educational placeholder
                "30_day_change": "neutral",
                "significance": "Active addresses indicate network usage and adoption",
                "explanation": "The number of unique active addresses shows how many users are actively using the network, serving as a proxy for adoption and engagement."
            },
            "new_addresses": {
                "current_trend": "moderately_increasing",
                "significance": "New address creation indicates user growth",
                "explanation": "Growth in new addresses suggests ongoing user acquisition and network expansion, though some addresses may belong to existing users."
            },
            "network_utilization": {
                "current_level": "moderate",
                "significance": "Network utilization shows demand for block space",
                "explanation": "High network utilization can indicate strong demand for transactions, potentially leading to higher fees during peak periods."
            },
            "dapp_activity": {
                "trend": "growing",
                "significance": "DeFi and application usage drives network demand",
                "explanation": "Decentralized application activity generates transactions and demonstrates practical utility of the network."
            }
        }
        
        activity_assessment = self._assess_activity_trends(activity_metrics)
        
        return {
            "metrics": activity_metrics,
            "overall_activity": activity_assessment,
            "growth_indicators": self._identify_growth_indicators(activity_metrics),
            "usage_patterns": self._analyze_usage_patterns(activity_metrics),
            "educational_notes": [
                "Network activity metrics provide insights into real usage vs speculation",
                "Active addresses can be influenced by market conditions and user behavior",
                "Network utilization affects transaction costs and user experience",
                "DApp activity demonstrates practical utility beyond simple transfers"
            ]
        }
    
    def _analyze_holder_behavior(self) -> Dict[str, Any]:
        """
        Analyze holder behavior and distribution patterns.
        
        Returns:
            Dictionary with holder behavior analysis
        """
        holder_metrics = {
            "holder_distribution": {
                "retail_holders": "increasing",
                "whale_concentration": "stable",
                "institutional_holdings": "growing",
                "explanation": "Holder distribution shows how tokens are distributed across different holder types, which can indicate market maturity and stability."
            },
            "holding_periods": {
                "short_term": "decreasing",
                "medium_term": "stable",
                "long_term": "increasing",
                "explanation": "Holding period analysis reveals investor sentiment and conviction levels across different time horizons."
            },
            "profit_loss_status": {
                "in_profit": "moderate_percentage",
                "in_loss": "moderate_percentage",
                "break_even": "small_percentage",
                "explanation": "The percentage of holders in profit or loss can influence selling pressure and market dynamics."
            },
            "accumulation_distribution": {
                "current_phase": "accumulation",
                "accumulation_zones": "identified",
                "distribution_zones": "minimal",
                "explanation": "Accumulation and distribution patterns show how different holder groups are positioning themselves over time."
            }
        }
        
        behavior_insights = self._analyze_holder_patterns(holder_metrics)
        
        return {
            "metrics": holder_metrics,
            "behavioral_insights": behavior_insights,
            "market_maturity": self._assess_market_maturity(holder_metrics),
            "risk_indicators": self._identify_holder_risks(holder_metrics),
            "educational_context": [
                "Holder behavior provides insights into market psychology",
                "Distribution patterns can indicate market structure changes",
                "Long-term holder accumulation often signals conviction",
                "Whale activity can significantly impact market dynamics"
            ]
        }
    
    def _analyze_transaction_metrics(self) -> Dict[str, Any]:
        """
        Analyze transaction-related metrics.
        
        Returns:
            Dictionary with transaction metrics analysis
        """
        transaction_metrics = {
            "transaction_volume": {
                "daily_volume": "stable",
                "volume_trend": "sideways",
                "value_transferred": "moderate",
                "explanation": "Transaction volume measures the total value being moved on-chain, reflecting economic activity and network utilization."
            },
            "transaction_count": {
                "daily_count": "stable",
                "count_trend": "slightly_increasing",
                "average_transaction_size": "decreasing",
                "explanation": "Transaction count shows network usage frequency, while average size can indicate usage patterns and efficiency."
            },
            "transaction_fees": {
                "average_fee": "moderate",
                "fee_trend": "stable",
                "fee_pressure": "low",
                "explanation": "Transaction fees reflect network demand and can influence user behavior, especially for smaller transactions."
            },
            "transaction_types": {
                "simple_transfers": "majority",
                "smart_contract_interactions": "growing",
                "exchange_transactions": "stable",
                "explanation": "Transaction type analysis shows how the network is being used and what activities drive demand."
            }
        }
        
        transaction_insights = self._analyze_transaction_patterns(transaction_metrics)
        
        return {
            "metrics": transaction_metrics,
            "transaction_insights": transaction_insights,
            "efficiency_metrics": self._analyze_efficiency(transaction_metrics),
            "economic_activity": self._assess_economic_activity(transaction_metrics),
            "educational_notes": [
                "Transaction metrics provide insights into real economic activity",
                "Fee analysis helps understand network congestion and user costs",
                "Transaction types reveal how the network is being utilized",
                "Volume patterns can indicate market sentiment and activity"
            ]
        }
    
    def _analyze_network_health(self) -> Dict[str, Any]:
        """
        Analyze network health and security metrics.
        
        Returns:
            Dictionary with network health analysis
        """
        health_metrics = {
            "network_security": {
                "hash_rate": "stable",  # For PoW networks
                "staking_participation": "healthy",  # For PoS networks
                "decentralization_level": "good",
                "explanation": "Network security metrics show how robust and resilient the network is against attacks and centralization."
            },
            "network_performance": {
                "block_time_consistency": "stable",
                "confirmation_time": "normal",
                "network_latency": "acceptable",
                "explanation": "Performance metrics indicate how well the network is functioning and providing reliable service to users."
            },
            "development_activity": {
                "developer_contribution": "active",
                "code_updates": "regular",
                "ecosystem_growth": "expanding",
                "explanation": "Development activity shows the long-term viability and innovation capacity of the network."
            },
            "ecosystem_metrics": {
                "node_count": "stable",
                "client_diversity": "good",
                "geographic_distribution": "diverse",
                "explanation": "Ecosystem metrics indicate network decentralization and resilience against single points of failure."
            }
        }
        
        health_assessment = self._assess_network_vitality(health_metrics)
        
        return {
            "metrics": health_metrics,
            "overall_health": health_assessment,
            "security_analysis": self._analyze_security_posture(health_metrics),
            "sustainability_factors": self._assess_sustainability(health_metrics),
            "educational_insights": [
                "Network health is fundamental to long-term viability",
                "Security metrics ensure network integrity and user trust",
                "Development activity indicates ongoing innovation and maintenance",
                "Ecosystem diversity contributes to network resilience"
            ]
        }
    
    def _generate_onchain_insights(
        self,
        activity: Dict[str, Any],
        holders: Dict[str, Any],
        transactions: Dict[str, Any],
        health: Dict[str, Any]
    ) -> List[str]:
        """
        Generate key insights from on-chain analysis.
        
        Args:
            activity: Network activity analysis
            holders: Holder behavior analysis
            transactions: Transaction metrics analysis
            health: Network health analysis
            
        Returns:
            List of key insights
        """
        insights = []
        
        # Activity insights
        if activity["overall_activity"]["trend"] == "growing":
            insights.append("Growing network activity suggests increasing adoption and utility")
        elif activity["overall_activity"]["trend"] == "declining":
            insights.append("Declining activity may indicate reduced usage or market fatigue")
        
        # Holder insights
        if holders["behavioral_insights"]["long_term_trend"] == "accumulation":
            insights.append("Long-term holder accumulation suggests conviction in network fundamentals")
        elif holders["behavioral_insights"]["distribution_pattern"] == "distribution":
            insights.append("Distribution from long-term holders may indicate profit-taking or reduced conviction")
        
        # Transaction insights
        if transactions["economic_activity"]["trend"] == "increasing":
            insights.append("Rising transaction volume indicates growing economic activity on-chain")
        elif transactions["efficiency_metrics"]["fee_pressure"] == "high":
            insights.append("High fee pressure may constrain smaller transactions and affect user experience")
        
        # Health insights
        if health["overall_health"]["status"] == "strong":
            insights.append("Strong network health provides foundation for long-term growth")
        elif health["overall_health"]["status"] == "concerning":
            insights.append("Network health concerns may require attention for sustainable development")
        
        return insights
    
    def _assess_network_conditions(
        self,
        activity: Dict[str, Any],
        holders: Dict[str, Any],
        transactions: Dict[str, Any],
        health: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess overall network conditions.
        
        Args:
            activity: Network activity analysis
            holders: Holder behavior analysis
            transactions: Transaction metrics analysis
            health: Network health analysis
            
        Returns:
            Overall network conditions assessment
        """
        condition_factors = {
            "activity_trend": activity["overall_activity"]["trend"],
            "holder_sentiment": holders["behavioral_insights"]["overall_sentiment"],
            "transaction_health": transactions["economic_activity"]["status"],
            "network_vitality": health["overall_health"]["status"]
        }
        
        # Determine overall conditions
        positive_factors = sum(1 for v in condition_factors.values() if v in ["growing", "accumulation", "healthy", "strong"])
        negative_factors = sum(1 for v in condition_factors.values() if v in ["declining", "distribution", "unhealthy", "weak"])
        
        if positive_factors > negative_factors:
            overall_status = "positive"
        elif negative_factors > positive_factors:
            overall_status = "negative"
        else:
            overall_status = "neutral"
        
        return {
            "overall_status": overall_status,
            "key_factors": condition_factors,
            "strengths": self._identify_network_strengths(condition_factors),
            "concerns": self._identify_network_concerns(condition_factors),
            "outlook": "stable"
        }
    
    def _assess_activity_trends(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall activity trends."""
        return {
            "trend": "stable",
            "strength": "moderate",
            "sustainability": "likely_sustainable"
        }
    
    def _identify_growth_indicators(self, metrics: Dict[str, Any]) -> List[str]:
        """Identify growth indicators from activity metrics."""
        return [
            "New address creation shows user acquisition",
            "DApp activity demonstrates utility beyond speculation",
            "Network utilization indicates demand for services"
        ]
    
    def _analyze_usage_patterns(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze usage patterns."""
        return {
            "primary_usage": "transfers_and_dapps",
            "user_engagement": "moderate",
            "retention_indicators": "positive"
        }
    
    def _analyze_holder_patterns(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze holder behavior patterns."""
        return {
            "long_term_trend": "accumulation",
            "distribution_pattern": "stable",
            "overall_sentiment": "cautiously_optimistic"
        }
    
    def _assess_market_maturity(self, metrics: Dict[str, Any]) -> str:
        """Assess market maturity based on holder metrics."""
        return "maturing"
    
    def _identify_holder_risks(self, metrics: Dict[str, Any]) -> List[str]:
        """Identify potential risks from holder metrics."""
        return [
            "Concentration risk if whale holdings increase",
            "Liquidity risk if long-term holders start distributing",
            "Volatility risk if short-term holders dominate"
        ]
    
    def _analyze_transaction_patterns(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze transaction patterns."""
        return {
            "volume_trend": "stable",
            "efficiency_trend": "improving",
            "usage_evolution": "maturing"
        }
    
    def _analyze_efficiency(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze transaction efficiency."""
        return {
            "fee_efficiency": "good",
            "throughput_utilization": "moderate",
            "cost_effectiveness": "reasonable"
        }
    
    def _assess_economic_activity(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Assess economic activity level."""
        return {
            "status": "moderate",
            "trend": "stable",
            "quality": "improving"
        }
    
    def _assess_network_vitality(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall network vitality."""
        return {
            "status": "healthy",
            "strength": "strong",
            "resilience": "good"
        }
    
    def _analyze_security_posture(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze network security posture."""
        return {
            "overall_security": "strong",
            "attack_resistance": "high",
            "decentralization": "adequate"
        }
    
    def _assess_sustainability(self, metrics: Dict[str, Any]) -> List[str]:
        """Assess sustainability factors."""
        return [
            "Active development ensures continuous improvement",
            "Diverse ecosystem reduces single points of failure",
            "Healthy economic incentives support network security"
        ]
    
    def _identify_network_strengths(self, factors: Dict[str, Any]) -> List[str]:
        """Identify network strengths."""
        strengths = []
        for factor, value in factors.items():
            if value in ["growing", "accumulation", "healthy", "strong"]:
                strengths.append(f"{factor.replace('_', ' ').title()}: {value}")
        return strengths
    
    def _identify_network_concerns(self, factors: Dict[str, Any]) -> List[str]:
        """Identify network concerns."""
        concerns = []
        for factor, value in factors.items():
            if value in ["declining", "distribution", "unhealthy", "weak"]:
                concerns.append(f"{factor.replace('_', ' ').title()}: {value}")
        return concerns
    
    def _get_educational_explanations(self) -> List[str]:
        """Get educational explanations about on-chain analysis."""
        return [
            "On-chain metrics provide transparent insights into network activity",
            "Blockchain data allows for unprecedented market analysis capabilities",
            "Network fundamentals often diverge from price action in short term",
            "Long-term value correlates with network utility and adoption",
            "On-chain analysis complements traditional market analysis methods",
            "Understanding blockchain metrics helps assess project fundamentals"
        ]
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    
    def _error_response(self, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            "error": True,
            "message": f"On-chain analysis failed: {error_message}",
            "educational_explanations": self._get_educational_explanations()
        }
