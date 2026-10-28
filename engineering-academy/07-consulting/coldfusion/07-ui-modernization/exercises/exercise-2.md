# Exercise 2: React Frontend with CF Backend

> Build a React component that calls a ColdFusion REST API.

## Objective

Learn to integrate React with ColdFusion REST APIs.

## Scenario

**Application:** Product catalog
**Goal:** React UI with CF REST backend

## Instructions

### Part 1: ColdFusion REST API

Create the CF REST component:

```cfml
component restpath="/api/products" rest="true" {
    
    // Enable REST
    this.restEnabled = true;
    
    // GET /api/products - List all products
    remote array function getProducts() httpmethod="GET" {
        local.products = queryExecute(
            "SELECT id, name, description, price, stock 
             FROM products 
             ORDER BY name"
        );
        
        return entityToQuery(local.products).toQueryObject();
    }
    
    // GET /api/products/:id - Get single product
    remote struct function getProduct(required numeric id restargSource="path") httpmethod="GET" {
        local.product = queryExecute(
            "SELECT * FROM products WHERE id = ?",
            [arguments.id]
        );
        
        if (local.product.recordCount == 0) {
            restSetResponse({
                status: 404,
                headers: {"Content-Type": "application/json"},
                content: '{"error": "Product not found"}'
            });
            return {};
        }
        
        return local.product.toQueryObject()[1];
    }
    
    // POST /api/products - Create product
    remote struct function createProduct(required struct data httpmethod="POST" restargsource="body") {
        
        // Validation
        if (!structKeyExists(arguments.data, "name") || !len(arguments.data.name)) {
            restSetResponse({
                status: 400,
                content: '{"error": "Name is required"}'
            });
            return {};
        }
        
        local.result = queryExecute(
            "INSERT INTO products (name, description, price, stock) 
             VALUES (?, ?, ?, ?)
             SELECT SCOPE_IDENTITY() as id",
            [arguments.data.name, arguments.data.description ?: "", 
             arguments.data.price ?: 0, arguments.data.stock ?: 0]
        );
        
        restSetResponse({status: 201});
        return getProduct(local.result.id);
    }
    
}
```

### Part 2: React Component

Create the ProductList component:

```jsx
// ProductList.jsx
import React, { useState, useEffect } from 'react';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const API_URL = 'http://localhost:8500/rest/api/products';
    
    useEffect(() => {
        fetchProducts();
    }, []);
    
    const fetchProducts = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            setProducts(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    
    if (loading) return <div>Loading...
... [truncated for context limit]