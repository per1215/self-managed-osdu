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
    describe('SchemaInfo', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.SchemaInfo();
      });

      it('should create an instance of SchemaInfo', function() {
        // TODO: update the code to test SchemaInfo
        expect(instance).to.be.a(SelfManagedOsdu.SchemaInfo);
      });

      it('should have the property createdBy (base name: "createdBy")', function() {
        // TODO: update the code to test the property createdBy
        expect(instance).to.have.property('createdBy');
        // expect(instance.createdBy).to.be(expectedValueLiteral);
      });

      it('should have the property dateCreated (base name: "dateCreated")', function() {
        // TODO: update the code to test the property dateCreated
        expect(instance).to.have.property('dateCreated');
        // expect(instance.dateCreated).to.be(expectedValueLiteral);
      });

      it('should have the property schemaIdentity (base name: "schemaIdentity")', function() {
        // TODO: update the code to test the property schemaIdentity
        expect(instance).to.have.property('schemaIdentity');
        // expect(instance.schemaIdentity).to.be(expectedValueLiteral);
      });

      it('should have the property scope (base name: "scope")', function() {
        // TODO: update the code to test the property scope
        expect(instance).to.have.property('scope');
        // expect(instance.scope).to.be(expectedValueLiteral);
      });

      it('should have the property status (base name: "status")', function() {
        // TODO: update the code to test the property status
        expect(instance).to.have.property('status');
        // expect(instance.status).to.be(expectedValueLiteral);
      });

      it('should have the property supersededBy (base name: "supersededBy")', function() {
        // TODO: update the code to test the property supersededBy
        expect(instance).to.have.property('supersededBy');
        // expect(instance.supersededBy).to.be(expectedValueLiteral);
      });

    });
  });

}));
