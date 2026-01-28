"""
FastAPI application for MacroChain AI.

This module provides the web API interface for the MacroChain AI
cryptocurrency market analysis system.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import logging
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.analyzer import MacroChainAnalyzer
from services.response_formatter import ResponseFormatter
from config.settings import get_api_config


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
api_config = get_api_config()
app = FastAPI(
    title=api_config["title"],
    description=api_config["description"],
    version=api_config["version"]
)

# Initialize components
analyzer = MacroChainAnalyzer()
formatter = ResponseFormatter()


# Pydantic models for request/response
class AnalysisRequest(BaseModel):
    """Request model for market analysis."""
    query: str
    assets: Optional[List[str]] = None


class AnalysisResponse(BaseModel):
    """Response model for market analysis."""
    query: str
    timestamp: str
    summary: str
    market_conditions: Dict[str, Any]
    analysis_sections: Dict[str, Any]
    key_insights: List[str]
    risk_factors: List[str]
    educational_context: str
    disclaimer: str
    metadata: Dict[str, Any]


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str
    timestamp: str
    version: str
    components: Dict[str, str]


@app.get("/", response_model=Dict[str, str])
async def root():
    """
    Root endpoint with basic information.
    
    Returns:
        Basic API information
    """
    return {
        "message": "MacroChain AI - Cryptocurrency Market Analysis API",
        "description": "Educational crypto market analysis without financial advice",
        "version": api_config["version"],
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        System health status
    """
    try:
        from datetime import datetime
        
        components = {
            "analyzer": "healthy",
            "formatter": "healthy",
            "api": "healthy"
        }
        
        return HealthResponse(
            status="healthy",
            timestamp=datetime.utcnow().isoformat() + "Z",
            version=api_config["version"],
            components=components
        )
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Health check failed")


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_market(request: AnalysisRequest):
    """
    Analyze cryptocurrency market based on user query.
    
    Args:
        request: Analysis request containing query and optional assets
        
    Returns:
        Comprehensive market analysis response
        
    Raises:
        HTTPException: If analysis fails
    """
    try:
        logger.info(f"Received analysis request: {request.query}")
        
        # Validate query
        if not request.query or len(request.query.strip()) < 3:
            raise HTTPException(
                status_code=400, 
                detail="Query must be at least 3 characters long"
            )
        
        # Validate assets if provided
        if request.assets:
            if len(request.assets) > 10:
                raise HTTPException(
                    status_code=400,
                    detail="Maximum 10 assets allowed per request"
                )
            
            # Convert to lowercase for consistency
            assets = [asset.lower().strip() for asset in request.assets if asset.strip()]
        else:
            assets = None
        
        # Perform analysis
        analysis_result = analyzer.analyze(request.query, assets)
        
        # Check for analysis errors
        if analysis_result.get("error"):
            raise HTTPException(
                status_code=500,
                detail=f"Analysis failed: {analysis_result.get('message', 'Unknown error')}"
            )
        
        # Format response
        formatted_response = formatter.format_analysis_response(
            analysis_result, 
            request.query
        )
        
        logger.info("Analysis completed successfully")
        return formatted_response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis request failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error during analysis: {str(e)}"
        )


@app.get("/info", response_model=Dict[str, Any])
async def get_info():
    """
    Get information about the API and analysis capabilities.
    
    Returns:
        API information and capabilities
    """
    try:
        return {
            "name": "MacroChain AI",
            "description": "AI-powered cryptocurrency market analysis agent",
            "purpose": "Educational market analysis without financial advice",
            "capabilities": [
                "Macroeconomic analysis",
                "Market sentiment analysis", 
                "On-chain metrics analysis",
                "Educational insights",
                "Risk factor identification"
            ],
            "supported_assets": [
                "bitcoin",
                "ethereum", 
                "major cryptocurrencies"
            ],
            "analysis_types": [
                "macroeconomic",
                "sentiment",
                "onchain",
                "combined"
            ],
            "limitations": [
                "Educational purposes only",
                "No financial advice provided",
                "No price predictions",
                "No trading signals",
                "Conceptual analysis framework"
            ],
            "disclaimer": (
                "This tool is for educational purposes only and does not constitute "
                "financial advice. Cryptocurrency markets are highly volatile and risky."
            ),
            "version": api_config["version"],
            "endpoints": {
                "analyze": "POST /analyze - Perform market analysis",
                "health": "GET /health - Check system health",
                "info": "GET /info - Get API information",
                "docs": "GET /docs - API documentation"
            }
        }
    except Exception as e:
        logger.error(f"Info request failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve API information: {str(e)}"
        )


@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handle 404 errors."""
    return {
        "error": "Endpoint not found",
        "message": f"The requested endpoint {request.url.path} does not exist",
        "available_endpoints": ["/", "/health", "/analyze", "/info", "/docs"],
        "timestamp": formatter._get_timestamp()
    }


@app.exception_handler(422)
async def validation_error_handler(request, exc):
    """Handle validation errors."""
    return {
        "error": "Validation error",
        "message": "Request validation failed. Please check your input parameters.",
        "details": str(exc),
        "timestamp": formatter._get_timestamp()
    }


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handle internal server errors."""
    logger.error(f"Internal server error: {str(exc)}")
    return {
        "error": "Internal server error",
        "message": "An unexpected error occurred while processing your request.",
        "timestamp": formatter._get_timestamp()
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Handle application startup."""
    logger.info("MacroChain AI API starting up...")
    logger.info(f"API version: {api_config['version']}")
    logger.info("Documentation available at: /docs")
    logger.info("MacroChain AI API ready to serve requests")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Handle application shutdown."""
    logger.info("MacroChain AI API shutting down...")


if __name__ == "__main__":
    import uvicorn
    
    # Run the application
    uvicorn.run(
        "app:app",
        host=api_config["host"],
        port=api_config["port"],
        reload=True,
        log_level="info"
    )
