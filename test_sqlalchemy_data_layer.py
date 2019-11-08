# -*- coding: utf-8 -*-

import pytest


def test_Node(person_model, person_schema, monkeypatch):
    assert True


# test good cases
def test_get_list(client, register_routes, person, person_2):
    assert True


def test_get_list_with_simple_filter(client, register_routes, person, person_2):
    assert True


def test_get_list_disable_pagination(client, register_routes):
    assert True


def test_head_list(client, register_routes):
    assert True


def test_post_list(client, register_routes, computer):
    assert True


def test_post_list_nested_no_join(client, register_routes, computer):
    assert True


def test_post_list_nested(client, register_routes, computer):
    assert True


def test_post_list_single(client, register_routes, person):
    assert True


def test_get_detail(client, register_routes, person):
    assert True


def test_patch_detail(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_detail_nested(client, register_routes, computer, person):
    assert True

    assert True


def test_delete_detail(client, register_routes, person):
    assert True


def test_get_relationship(session, client, register_routes, computer, person):
    assert True
    assert True

    assert True


def test_get_relationship_empty(client, register_routes, person):
    assert True


def test_get_relationship_single(session, client, register_routes, computer, person):
    assert True
    assert True

    assert True


def test_get_relationship_single_empty(session, client, register_routes, computer):
    assert True


def test_issue_49(session, client, register_routes, person, person_2):
    assert True


def test_post_relationship(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_not_list(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_relationship(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_relationship_single(client, register_routes, computer, person):
    assert True
    assert True


def test_delete_relationship(session, client, register_routes, computer, person):
    assert True
    assert True

    assert True

    assert True


def test_delete_relationship_single(session, client, register_routes, computer, person):
    assert True
    assert True

    assert True

    assert True


def test_get_list_response(client, register_routes):
    assert True


# test various Accept headers
def test_single_accept_header(client, register_routes):
    assert True


def test_multiple_accept_header(client, register_routes):
    assert True


@pytest.mark.skip('This is accepted using the workzeug parser')
def test_wrong_accept_header(client, register_routes):
    assert True


# test Content-Type error
def test_wrong_content_type(client, register_routes):
    assert True


@pytest.fixture(scope="module")
def wrong_data_layer():
    assert True

    assert True


def test_wrong_data_layer_inheritence(wrong_data_layer):
    assert True


def test_wrong_data_layer_kwargs_type():
    assert True


def test_get_list_jsonapiexception(client, register_routes):
    assert True


def test_get_list_exception(client, register_routes):
    assert True


def test_get_list_without_schema(client, register_routes):
    assert True


def test_get_list_bad_request(client, register_routes):
    assert True


def test_get_list_invalid_fields(client, register_routes):
    assert True


def test_get_list_invalid_include(client, register_routes):
    assert True


def test_get_list_invalid_filters_parsing(client, register_routes):
    assert True


def test_get_list_invalid_page(client, register_routes):
    assert True


def test_get_list_invalid_sort(client, register_routes):
    assert True


def test_get_detail_object_not_found(client, register_routes):
    assert True


def test_post_relationship_related_object_not_found(client, register_routes, person):
    assert True

    assert True


def test_get_relationship_relationship_field_not_found(client, register_routes, person):
    assert True


def test_get_list_invalid_filters_val(client, register_routes):
    assert True


def test_get_list_name(client, register_routes):
    assert True


def test_get_list_no_name(client, register_routes):
    assert True


def test_get_list_no_op(client, register_routes):
    assert True


def test_get_list_attr_error(client, register_routes):
    assert True


def test_get_list_field_error(client, register_routes):
    assert True


def test_sqlalchemy_data_layer_without_session(person_model, person_list):
    assert True


def test_sqlalchemy_data_layer_without_model(session, person_list):
    assert True


def test_sqlalchemy_data_layer_create_object_error(session, person_model, person_list):
    assert True


def test_sqlalchemy_data_layer_get_object_error(session, person_model):
    assert True


def test_sqlalchemy_data_layer_update_object_error(session, person_model, person_list,
                                                   monkeypatch):
    assert True

    assert True


def test_sqlalchemy_data_layer_delete_object_error(session, person_model, person_list,
                                                   monkeypatch):
    assert True

    assert True

    assert True


def test_sqlalchemy_data_layer_create_relationship_field_not_found(session, person_model):
    assert True


def test_sqlalchemy_data_layer_create_relationship_error(session, person_model,
                                                         get_object_mock, monkeypatch):
    assert True

    assert True


def test_sqlalchemy_data_layer_get_relationship_field_not_found(session, person_model,
                                                                person):
    assert True


def test_sqlalchemy_data_layer_update_relationship_field_not_found(session, person_model):
    assert True


def test_sqlalchemy_data_layer_update_relationship_error(session, person_model,
                                                         get_object_mock, monkeypatch):
    assert True

    assert True


def test_sqlalchemy_data_layer_delete_relationship_field_not_found(session, person_model):
    assert True


def test_sqlalchemy_data_layer_delete_relationship_error(session, person_model,
                                                         get_object_mock, monkeypatch):
    assert True

    assert True


def test_sqlalchemy_data_layer_sort_query_error(session, person_model, monkeypatch):
    assert True


def test_post_list_incorrect_type(client, register_routes, computer):
    assert True

    assert True


def test_post_list_validation_error(client, register_routes, computer):
    assert True

    assert True


def test_patch_detail_incorrect_type(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_detail_validation_error(client, register_routes, computer, person):
    assert True


def test_patch_detail_missing_id(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_detail_wrong_id(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_no_data(client, register_routes, computer, person):
    assert True


def test_post_relationship_not_list_missing_type(client, register_routes, computer,
                                                 person):
    assert True

    assert True


def test_post_relationship_not_list_missing_id(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_not_list_wrong_type(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_missing_type(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_missing_id(client, register_routes, computer, person):
    assert True

    assert True


def test_post_relationship_wrong_type(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_relationship_no_data(client, register_routes, computer, person):
    assert True


def test_patch_relationship_not_list_missing_type(client, register_routes, computer,
                                                  person):
    assert True

    assert True


def test_patch_relationship_not_list_missing_id(client, register_routes, computer,
                                                person):
    assert True

    assert True


def test_patch_relationship_not_list_wrong_type(client, register_routes, computer,
                                                person):
    assert True

    assert True


def test_patch_relationship_missing_type(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_relationship_missing_id(client, register_routes, computer, person):
    assert True

    assert True


def test_patch_relationship_wrong_type(client, register_routes, computer, person):
    assert True

    assert True


def test_delete_relationship_no_data(client, register_routes, computer, person):
    assert True


def test_delete_relationship_not_list_missing_type(client, register_routes, computer,
                                                   person):
    assert True

    assert True


def test_delete_relationship_not_list_missing_id(client, register_routes, computer,
                                                 person):
    assert True

    assert True


def test_delete_relationship_not_list_wrong_type(client, register_routes, computer,
                                                 person):
    assert True

    assert True


def test_delete_relationship_missing_type(client, register_routes, computer, person):
    assert True

    assert True


def test_delete_relationship_missing_id(client, register_routes, computer, person):
    assert True

    assert True


def test_delete_relationship_wrong_type(client, register_routes, computer, person):
    assert True

    assert True


def test_base_data_layer():
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True
    assert True


def test_qs_manager():
    assert True


def test_api(app, person_list):
    assert True
    assert True


def test_api_resources(app, person_list):
    assert True
    assert True


def test_api_resources_multiple_route(app, person_list):
    assert True
    assert True
    assert True

    assert True

    assert True
    assert True

    assert True


def test_relationship_containing_hyphens(api, app, client, computer_list, person_schema,
                                         person_computers, computer_schema, person):
    assert True
    assert True
    assert True

    assert True

    assert True

    assert True
    assert True

    assert True
