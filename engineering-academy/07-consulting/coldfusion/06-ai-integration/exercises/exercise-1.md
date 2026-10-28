# Exercise 1: Basic Chatbot Integration

> Integrate Claude API with ColdFusion for a customer service chatbot.

## Objective

Learn to call external AI APIs from ColdFusion using CFHTTP.

## Scenario

**Application:** Customer service portal
**Goal:** Add an AI chatbot to answer common questions

## Instructions

### Part 1: API Setup

Document your configuration:

```cfml
// Application configuration
variables.apiEndpoint = "https://api.anthropic.com/v1/messages";
variables.apiKey = serverSystem.ENV.CLAUDE_API_KEY;  // Set in environment
variables.model = "claude-3-5-sonnet-20241022";
```

### Part 2: CFHTTP Integration

Create a service component:

```cfml
component {
    
    variables.apiEndpoint = "https://api.anthropic.com/v1/messages";
    variables.apiKey = "";
    variables.model = "claude-3-5-sonnet-20241022";
    
    public struct function sendMessage(required string message, array history = []) {
        
        // Build the request payload
        local.payload = {
            model: variables.model,
            max_tokens: 1024,
            messages: []
        };
        
        // Add conversation history
        for (local.item in arguments.history) {
            local.payload.messages.append({
                role: local.item.role,
                content: local.item.content
            });
        }
        
        // Add current message
        local.payload.messages.append({
            role: "user",
            content: arguments.message
        });
        
        // Make the API call
        try {
            local.result = cfhttp(method="POST", 
                                  url=variables.apiEndpoint, 
                                  result="local.httpResult") {
                cfhttpparam(type="header", name="x-api-key", value=variables.apiKey);
                cfhttpparam(type="header", name="anthropic-version", value="2023-06-01");
                cfhttpparam(type="header", name="content-type", value="application/json");
                cfhttpparam(type="body", value=serializeJSON(local.payload));
            }
            
            if (local.httpResult.statusCode == "200 OK") {
                local.response = deserializeJSON(local.httpResult.fileContent);
                return {
                    success: true,
                    message: local.response.content[1].text
                };
            } else {
                return {
                    success: false,
                    error: "API error: " & local.httpResult.statusCode
                };
            }
        } catch (any e) {
            return {
                success: false,
                error: e.message
            };
        }
    }
}
```

### Part 3: Error Handling

Add proper error handling:

| Error Type | How to Handle |
|------------|--------------|
| API timeout | |
| Invalid API key | |
| Rate limiting | |
| Invalid response | |

### Part 4: Session Management

Design the conversation storage:

```cfml
// Store conversation in session scope
public void function saveConversation(required string userId, required array history) {
    
    // What storage approach?
    
    _______________________________________________________________
    
}

// Load conversation
public array function loadConversation(required string userId) {
    
    _______________________________________________________________
    
}
```

### Part 5: Frontend Integration

Create a simple chat interface:

```html
<!-- chat.cfm -->
<cfoutput>
<div id="chat-container">
    <div id="chat-history"></div>
    <form id="chat-form">
        <input type="text" id="message" placeholder="Ask a question...">
        <button type="submit">Send</button>
    </form>
</div>

<script>
document.getElementById('chat-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const message = document.getElementById('message').value;
    document.getElementById('message').value = '';
    
    // Add user message to UI
    $('#('#chat-history#').append('<div class="user">#JSStringFormat(message)#</div>');
    
    // Call CF API
    const response = await fetch('api/chat.cfc?method=sendMessage', {
        method: 'POST',
        body: JSON.stringify({ message: message })
    });
    
    const result = await response.json();
    
    // Add AI response to UI
    $('#('#chat-history#').append('<div class="ai">' + result.message + '</div>');
});
</script>
</cfoutput>
```

## Expected Outcome

1. Working chatbot service component
2. Error handling implemented
3. Conversation storage designed
4. Frontend interface created

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| CFHTTP integration working | 25 |
| Error handling appropriate | 20 |
| Session management designed | 20 |
| Frontend functional | 20 |
| Security considered | 15 |
| **Total** | **100** |

**Passing Score:** 70/100
