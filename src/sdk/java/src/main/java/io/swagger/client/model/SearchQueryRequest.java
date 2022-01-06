/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.SearchSpatialFilter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Json object to query the Search API
 */
@ApiModel(description = "Json object to query the Search API")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2022-01-06T19:40:40.245Z")
public class SearchQueryRequest {
  @SerializedName("offset")
  private Integer offset = null;

  @SerializedName("kind")
  private String kind = null;

  @SerializedName("limit")
  private Integer limit = null;

  @SerializedName("query")
  private String query = null;

  @SerializedName("spatialFilter")
  private SearchSpatialFilter spatialFilter = null;

  @SerializedName("returnedFields")
  private List<String> returnedFields = null;

  public SearchQueryRequest offset(Integer offset) {
    this.offset = offset;
    return this;
  }

   /**
   * The starting offset from which to return results
   * minimum: 0
   * @return offset
  **/
  @ApiModelProperty(value = "The starting offset from which to return results")
  public Integer getOffset() {
    return offset;
  }

  public void setOffset(Integer offset) {
    this.offset = offset;
  }

  public SearchQueryRequest kind(String kind) {
    this.kind = kind;
    return this;
  }

   /**
   * The kind of the record to query e.g. &#39;tenant1:test:well:1.0.0&#39;.
   * @return kind
  **/
  @ApiModelProperty(required = true, value = "The kind of the record to query e.g. 'tenant1:test:well:1.0.0'.")
  public String getKind() {
    return kind;
  }

  public void setKind(String kind) {
    this.kind = kind;
  }

  public SearchQueryRequest limit(Integer limit) {
    this.limit = limit;
    return this;
  }

   /**
   * The maximum number of results to return from the given offset. If no limit is provided, then it will return 10 items. Max number of items which can be fetched by the query is 1000.
   * minimum: 0
   * @return limit
  **/
  @ApiModelProperty(value = "The maximum number of results to return from the given offset. If no limit is provided, then it will return 10 items. Max number of items which can be fetched by the query is 1000.")
  public Integer getLimit() {
    return limit;
  }

  public void setLimit(Integer limit) {
    this.limit = limit;
  }

  public SearchQueryRequest query(String query) {
    this.query = query;
    return this;
  }

   /**
   * The query string in Lucene query string syntax.
   * @return query
  **/
  @ApiModelProperty(value = "The query string in Lucene query string syntax.")
  public String getQuery() {
    return query;
  }

  public void setQuery(String query) {
    this.query = query;
  }

  public SearchQueryRequest spatialFilter(SearchSpatialFilter spatialFilter) {
    this.spatialFilter = spatialFilter;
    return this;
  }

   /**
   * Get spatialFilter
   * @return spatialFilter
  **/
  @ApiModelProperty(value = "")
  public SearchSpatialFilter getSpatialFilter() {
    return spatialFilter;
  }

  public void setSpatialFilter(SearchSpatialFilter spatialFilter) {
    this.spatialFilter = spatialFilter;
  }

  public SearchQueryRequest returnedFields(List<String> returnedFields) {
    this.returnedFields = returnedFields;
    return this;
  }

  public SearchQueryRequest addReturnedFieldsItem(String returnedFieldsItem) {
    if (this.returnedFields == null) {
      this.returnedFields = new ArrayList<String>();
    }
    this.returnedFields.add(returnedFieldsItem);
    return this;
  }

   /**
   * The fields on which to project the results.
   * @return returnedFields
  **/
  @ApiModelProperty(value = "The fields on which to project the results.")
  public List<String> getReturnedFields() {
    return returnedFields;
  }

  public void setReturnedFields(List<String> returnedFields) {
    this.returnedFields = returnedFields;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SearchQueryRequest searchQueryRequest = (SearchQueryRequest) o;
    return Objects.equals(this.offset, searchQueryRequest.offset) &&
        Objects.equals(this.kind, searchQueryRequest.kind) &&
        Objects.equals(this.limit, searchQueryRequest.limit) &&
        Objects.equals(this.query, searchQueryRequest.query) &&
        Objects.equals(this.spatialFilter, searchQueryRequest.spatialFilter) &&
        Objects.equals(this.returnedFields, searchQueryRequest.returnedFields);
  }

  @Override
  public int hashCode() {
    return Objects.hash(offset, kind, limit, query, spatialFilter, returnedFields);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SearchQueryRequest {\n");
    
    sb.append("    offset: ").append(toIndentedString(offset)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    limit: ").append(toIndentedString(limit)).append("\n");
    sb.append("    query: ").append(toIndentedString(query)).append("\n");
    sb.append("    spatialFilter: ").append(toIndentedString(spatialFilter)).append("\n");
    sb.append("    returnedFields: ").append(toIndentedString(returnedFields)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

