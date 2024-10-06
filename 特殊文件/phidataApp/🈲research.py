from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

# Create Tool instances
tool1 = Tool.objects.create(name="DuckDuckGo")
tool2 = Tool.objects.create(name="Newspaper4k")

# Create Instruction instances
instruction1 = Instruction.objects.create(text="For the provided topic, search for the top 3 links.")
instruction2 = Instruction.objects.create(text="Then read each URL and extract the article text, if a URL isn't available, ignore and let it be.")
instruction3 = Instruction.objects.create(text="Analyse and prepare an NYT worthy article based on the information.")

# Create AssistantInfo instance
assistant_info = AssistantInfo.objects.create(
    show_tool_calls=True,
    description="You are a senior NYT researcher writing an article on a topic.",
    add_datetime_to_instructions=True,
)

assistant_info.tools.add(tool1, tool2)
assistant_info.instructions.add(instruction1, instruction2, instruction3)

assistant = Assistant(
    tools=[DuckDuckGo(), Newspaper4k()],
    show_tool_calls=assistant_info.show_tool_calls,
    description=assistant_info.description,
    instructions=[instruction.text for instruction in assistant_info.instructions.all()],
    add_datetime_to_instructions=assistant_info.add_datetime_to_instructions,
)
assistant.print_response("Latest developments in AI", markdown=True)
