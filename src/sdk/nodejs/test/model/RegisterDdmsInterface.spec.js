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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SelfManagedOsdu);
  }
}(this, function(expect, SelfManagedOsdu) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('RegisterDdmsInterface', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.RegisterDdmsInterface();
      });

      it('should create an instance of RegisterDdmsInterface', function() {
        // TODO: update the code to test RegisterDdmsInterface
        expect(instance).to.be.a(SelfManagedOsdu.RegisterDdmsInterface);
      });

      it('should have the property entityType (base name: "entityType")', function() {
        // TODO: update the code to test the property entityType
        expect(instance).to.have.property('entityType');
        // expect(instance.entityType).to.be(expectedValueLiteral);
      });

      it('should have the property schema (base name: "schema")', function() {
        // TODO: update the code to test the property schema
        expect(instance).to.have.property('schema');
        // expect(instance.schema).to.be(expectedValueLiteral);
      });

    });
  });

}));