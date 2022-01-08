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
    define(['ApiClient', 'model/LegalTagInvalidResponse'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./LegalTagInvalidResponse'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.LegalTagInvalidResponseList = factory(root.SelfManagedOsdu.ApiClient, root.SelfManagedOsdu.LegalTagInvalidResponse);
  }
}(this, function(ApiClient, LegalTagInvalidResponse) {
  'use strict';

  /**
   * The LegalTagInvalidResponseList model module.
   * @module model/LegalTagInvalidResponseList
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>LegalTagInvalidResponseList</code>.
   * Represents a collection invalid LegalTags.
   * @alias module:model/LegalTagInvalidResponseList
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>LegalTagInvalidResponseList</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/LegalTagInvalidResponseList} obj Optional instance to populate.
   * @return {module:model/LegalTagInvalidResponseList} The populated <code>LegalTagInvalidResponseList</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('invalidLegalTags'))
        obj.invalidLegalTags = ApiClient.convertToType(data['invalidLegalTags'], [LegalTagInvalidResponse]);
    }
    return obj;
  }

  /**
   * A collection of invalid LegalTags.
   * @member {Array.<module:model/LegalTagInvalidResponse>} invalidLegalTags
   */
  exports.prototype.invalidLegalTags = undefined;


  return exports;

}));
