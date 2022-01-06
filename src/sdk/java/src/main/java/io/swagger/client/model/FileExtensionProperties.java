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
import java.io.IOException;

/**
 * Useful for providing the user defined attributes to be associated with the file metadata record.
 */
@ApiModel(description = "Useful for providing the user defined attributes to be associated with the file metadata record.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2022-01-06T19:53:30.442Z")
public class FileExtensionProperties {
  @SerializedName("kind")
  private String kind = null;

  public FileExtensionProperties kind(String kind) {
    this.kind = kind;
    return this;
  }

   /**
   * The schema ID for this schema fragment
   * @return kind
  **/
  @ApiModelProperty(example = "os:npd:csvFileExtDetails:1.0.0", value = "The schema ID for this schema fragment")
  public String getKind() {
    return kind;
  }

  public void setKind(String kind) {
    this.kind = kind;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileExtensionProperties fileExtensionProperties = (FileExtensionProperties) o;
    return Objects.equals(this.kind, fileExtensionProperties.kind);
  }

  @Override
  public int hashCode() {
    return Objects.hash(kind);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileExtensionProperties {\n");
    
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
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

