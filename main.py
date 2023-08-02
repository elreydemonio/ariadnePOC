from api import app, db

from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.graphql.queries import get_books_resolver
from api.graphql.mutations import create_book_resolver

query = ObjectType("Query")

mutation = ObjectType("Mutation")

query.set_field("getBooks", get_books_resolver)

mutation.set_field("createBook", create_book_resolver)

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(
	type_defs, query, mutation, snake_case_fallback_resolvers
)

explorer_html = ExplorerGraphiQL().html(None)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
	return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
	data = request.get_json()

	success, result = graphql_sync(
		schema,
		data,
		context_value=request,
		debug=app.debug
	)

	if success:
		status_code = 200
	else:
		status_code = 400

	return jsonify(result), status_code

if __name__ == "__main__":
	app.run()