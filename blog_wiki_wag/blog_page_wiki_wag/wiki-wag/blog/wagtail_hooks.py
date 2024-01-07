from wagtail import hooks

@hooks.register('construct_page')
def add_custom_context(request, page, context, *args, **kwargs):
    # Check if the page is a BlogPage and add additional context for tables
    if hasattr(page, 'body'):
        table_context = []
        for block in page.body:
            if block.block_type == 'table':
                # Sample logic for processing table data and adding CSS classes
                table_data = process_table_data(block.value)
                
                # Check conditions and add flags to the table data
                if some_condition:
                    table_data['is_red'] = True
                elif some_other_condition:
                    table_data['is_green'] = True

                table_context.append({'table_data': table_data})

        context['tables'] = table_context

    return context

def process_table_data(data):
    # Sample logic to process table data and return with added flags
    # Replace this with your own logic
    processed_table_data = {
        'data': data,
        'is_red': False,
        'is_green': False,
        # Other processed data...
    }

    # Add logic to set 'is_red' or 'is_green' based on conditions
    # For example:
    if some_condition:
        processed_table_data['is_red'] = True
    elif some_other_condition:
        processed_table_data['is_green'] = True

    return processed_table_data





