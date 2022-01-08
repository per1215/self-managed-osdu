/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.WorkflowTriggerRequest = factory(root.SelfManagedOsdu.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The WorkflowTriggerRequest model module.
   * @module model/WorkflowTriggerRequest
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>WorkflowTriggerRequest</code>.
   * @alias module:model/WorkflowTriggerRequest
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>WorkflowTriggerRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/WorkflowTriggerRequest} obj Optional instance to populate.
   * @return {module:model/WorkflowTriggerRequest} The populated <code>WorkflowTriggerRequest</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('runId'))
        obj.runId = ApiClient.convertToType(data['runId'], 'String');
      if (data.hasOwnProperty('executionContext'))
        obj.executionContext = ApiClient.convertToType(data['executionContext'], Object);
    }
    return obj;
  }

  /**
   * Optional. Explicit setting up workflow run id.
   * @member {String} runId
   */
  exports.prototype.runId = undefined;

  /**
   * Map to configure workflow speciffic key value pairs.
   * @member {Object} executionContext
   */
  exports.prototype.executionContext = undefined;


  return exports;

}));
