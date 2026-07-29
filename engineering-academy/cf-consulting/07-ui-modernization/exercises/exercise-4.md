# Exercise 4: Progressive Enhancement

> Implement a progressively enhanced search feature.

## Objective

Learn to build features that work without JavaScript but enhance with it.

## Scenario

**Application:** Product search
**Goal:** Works with and without JavaScript

## Instructions

### Part 1: HTML Form (Works Without JS)

```html
<!-- Pure HTML form - works without JS -->
<form method="GET" action="/search.cfm" class="search-form">
    <div class="input-group">
        <input type="search" 
               name="q" 
               value="<cfoutput>#encodeForHTML(url.q)#</cfoutput>"
               placeholder="Search products..."
               class="form-control"
               aria-label="Search products">
        <button type="submit" class="btn btn-primary">
            Search
        </button>
    </div>
</form>

<!-- Results (rendered server-side by ColdFusion) -->
<cfif structKeyExists(url, "q")>
    <cfoutput>
        <p>Found #rc.searchResults.recordCount# results for "#encodeForHTML(url.q)#"</p>
        
        <ul class="results-list">
            <cfloop query="rc.searchResults">
                <li class="result-item">
                    <h3><a href="/product.cfm?id=#id#">#encodeForHTML(name)#</a></h3>
                    <p>#encodeForHTML(description)#</p>
                </li>
            </cfloop>
        </ul>
    </cfoutput>
</cfif>
```

### Part 2: JavaScript Enhancement

```javascript
// search.js - Progressive enhancement
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.search-form');
    const input = form.querySelector('input[name="q"]');
    const resultsContainer = document.querySelector('.search-results');
    
    // If no results container exists, create one
    if (!resultsContainer) {
        resultsContainer = document.createElement('div');
        resultsContainer.className = 'search-results';
        form.insertAdjacentElement('afterend', resultsContainer);
    }
    
    // Debounce function
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Search function
    async function performSearch(query) {
        if (!query.trim()) {
            resultsContainer.innerHTML = '';
            return;
        }
        
        resultsContainer.innerHTML = '<div class="loading">Searching...</div>';
        
        try {
            const response = await fetch(`/api/search.cfm?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            
            renderResults(data);
        } catch (error) {
            resultsContainer.innerHTML = '<div class="error">Search failed. Showing server-side results.</div>';
            // Fall back to form submit
            form.submit();
        }
    }
    
    // Render results
    function renderResults(results) {
        if (!results.length) {
            resultsContainer.innerHTML = '<p class="no-results">No results found.</p>';
            return;
        }
        
        resultsContainer.innerHTML = `
            <p class="results-count">Found ${results.length} results</p>
            <ul class="results-list">
                ${results.map(r => `
                    <li class="result-item">
                        <h3><a href="/product.cfm?id=${r.id}">${escapeHtml(r.name)}</a></h3>
                        <p>${escapeHtml(r.description)}</p>
                    </li>
                `).join('')}
            </ul>
        `;
    }
    
    // Escape HTML to prevent XSS
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // Attach event listener with debounce
    input.addEventListener('input', debounce(e => performSearch(e.target.value), 300));
});
```

### Part 3: Testing Checklist

Complete the testing checklist:

| Test | JS Enabled | JS Disabled |
|------|-----------|-------------|
| Submit empty form | | |
| Submit with query | | |
| Type and wait | | |
| Network error during search | | |
| XSS attempt in query | | |
| Back button behavior | | |

---

## Expected Outcome

A search feature that:
- Works with form submit (no JS)
- Enhances with live search (JS enabled)
- Falls back gracefully on errors
- Is accessible and screen-reader friendly
