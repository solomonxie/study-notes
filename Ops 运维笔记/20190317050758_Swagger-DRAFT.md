# Swagger [DRAFT]

Swagger专门用来生成API，以内部API为主。

Swagger几大件：
- Swagger-Codegen

## Swagger vs. OpenAPI

[Refer to: What Is the Difference Between Swagger and OpenAPI?](https://swagger.io/blog/api-strategy/difference-between-swagger-and-openapi/)

The easiest way to understand the difference is:
- `OpenAPI` = Specification
- `Swagger` = Tools for **implementing** the specification

> "The OpenAPI is the official name of the specification. The development of the specification is fostered by the OpenAPI Initiative, which involves more the 30 organizations from different areas of the tech world — including Microsoft, Google, IBM, and CapitalOne. Smartbear Software, which is the company that leads the development of the Swagger tools, is also a member of the OpenAPI Initiative, helping lead the evolution of the specification."

`Swagger` is the name associated with some of the most well-known, and widely used tools for implementing the OpenAPI specification. The Swagger toolset includes a mix of open source, free, and commercial tools, which can be used at different stages of the API lifecycle.

These tools include:
- `Swagger Editor`: Swagger Editor lets you edit OpenAPI specifications in YAML inside your browser and to preview documentation in real time.
- `*Swagger UI`: Swagger UI is a collection of HTML, Javascript, and CSS assets that dynamically generate beautiful documentation from an OAS-compliant API.
- `*Swagger Codegen`: Allows generation of API client libraries (SDK generation), server stubs and documentation is automatically given an OpenAPI Spec.
- `Swagger Parser`: Standalone library for parsing OpenAPI definitions from Java
- `Swagger Core`: Java-related libraries for creating, consuming, and working with OpenAPI definitions
- `*Swagger Inspector` (free): API testing tool that lets you validate your APIs & generate OpenAPI definitions from an existing API
- `SwaggerHub` (free & commercial): API design and documentation, built for teams working with OpenAPI.
