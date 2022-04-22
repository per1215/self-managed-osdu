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


package osdu.client.model;

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
 * FileLocationRequest
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2022-01-08T01:37:46.955Z")
public class FileLocationRequest {
  @SerializedName("FileID")
  private String fileID = null;

  public FileLocationRequest fileID(String fileID) {
    this.fileID = fileID;
    return this;
  }

   /**
   * Get fileID
   * @return fileID
  **/
  @ApiModelProperty(value = "")
  public String getFileID() {
    return fileID;
  }

  public void setFileID(String fileID) {
    this.fileID = fileID;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileLocationRequest fileLocationRequest = (FileLocationRequest) o;
    return Objects.equals(this.fileID, fileLocationRequest.fileID);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fileID);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileLocationRequest {\n");
    
    sb.append("    fileID: ").append(toIndentedString(fileID)).append("\n");
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
