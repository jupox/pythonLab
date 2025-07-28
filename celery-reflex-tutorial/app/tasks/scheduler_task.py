from datetime import datetime
from app.celery_app import celery_app
from app.utils import get_supabase_client # Import the helper
from dotenv import load_dotenv
load_dotenv()
import os
import random

def insert_instruction_to_db(supabase, instruction, num_count, letter_count):
    insert_payload = {
        "code": instruction,
        "numbers": num_count,
        "letters": letter_count,
        "created_at": datetime.now().isoformat()
    }
    insert_response = supabase.table("codes").insert(insert_payload).execute()
    # Check for errors during insert
    if hasattr(insert_response, 'error') and insert_response.error:
        raise Exception(f"Failed to insert code: {insert_response.error.message}")
    if not insert_response.data: # Supabase often returns data on success
        print(f"Warning: Insert response for code {instruction}, Check database logs.")

def instruction_exists_in_db(supabase, instruction):
    """Check if the instruction code already exists in the supabase table."""
    existing_check_response = supabase.table("codes").select("code").eq("code", instruction).execute()

    # Check for errors during select
    if hasattr(existing_check_response, 'error') and existing_check_response.error:
        raise Exception(f"Failed to check existing code: {existing_check_response.error.message}")

    return not bool(existing_check_response.data)

@celery_app.task
def validate_instructions():
    """validate instruction from data.txt file."""
    if not os.path.isfile("data.txt"):
        return "Error: data.txt file does not exist."

    instructions = []
    with open("data.txt", "r") as file:
        instructions = file.readlines()

    if not instructions or len(instructions) <= 1:
        return "Error: Not enough instructions in the file to process."

    supabase = get_supabase_client()

    instructions = []
    with open("data.txt", "r") as file:
        instructions = file.readlines()

    instruction = instructions.pop(random.randint(0, len(instructions) - 1)).strip()

    # Validate if instruction starts with a number
    if not instruction or not instruction[0].isdigit():
        return f"Error: Instruction {instruction} does not start with a number."

    # Check for two numbers and two letters corresponding to alphabet positions
    num_count = 0
    letter_count = 0

    for char in instruction:
        if char.isdigit():
            num_count += 1
        elif char.isalpha() and 1 <= (ord(char.upper()) - ord('A') + 1) <= 26:
            letter_count += 1

    if num_count < 2 or letter_count < 2:
        return f"Error: Instruction {instruction} does not contain at least two numbers and two valid alphabet letters."

    if not instruction_exists_in_db(supabase, instruction):
        return f"Error: Instruction {instruction} already exists in the database."
    
    insert_instruction_to_db(supabase, instruction, num_count, letter_count)

    return f"validated instruction from data.txt file. Instruction is {instruction} {num_count} {letter_count}"
