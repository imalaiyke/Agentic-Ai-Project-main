#from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.agent_toolkits import SparkSQLToolkit, create_spark_sql_agent
from langchain_community.utilities.spark_sql import SparkSQL
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit
from pydantic import ConfigDict, Field


from langchain_community.tools.spark_sql.tool import (
    InfoSparkSQLTool,
    ListSparkSQLTool,
    QueryCheckerTool,
    QuerySparkSQLTool,
)
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools1=[QuerySparkSQLTool(db=self.db),
            InfoSparkSQLTool(db=self.db),
            ListSparkSQLTool(db=self.db),
            QueryCheckerTool(db=self.db),
            ]
    return tools1

def create_tool_node(tools1):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools1=tools1)
