from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import Exhibit, Artefact, AiSystemDescription, FailureDescription, LessonsLearned, ContributingFactors
from datetime import date
from unittest import mock


class ExhibitAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        # Mock the isCurator permission to always return True for tests
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit1 = Exhibit.objects.create(
            title="Test Exhibit 1",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.exhibit2 = Exhibit.objects.create(
            title="Test Exhibit 2",
            domain="Finance",
            backgroundDeploymentContext="Test context 2",
            intededUse="Test use 2",
            viewNumber=5
        )
        
    def test_get_all_exhibits_success(self):
        """Test retrieving all exhibits"""
        response = self.client.get('/api/exhibits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_get_single_exhibit_success(self):
        """Test retrieving a single exhibit"""
        response = self.client.get(f'/api/exhibits/{self.exhibit1.exhibitId}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Exhibit 1")
        
    def test_get_single_exhibit_not_found(self):
        """Test retrieving non-existent exhibit"""
        response = self.client.get('/api/exhibits/9999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_create_exhibit_success(self):
        """Test creating a new exhibit"""
        data = {
            'title': 'New Exhibit',
            'domain': 'Transportation',
            'backgroundDeploymentContext': 'New context',
            'intededUse': 'New use',
            'viewNumber': 0
        }
        response = self.client.post('/api/exhibits/viewCreate', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Exhibit.objects.count(), 3)
        
    def test_update_exhibit_success(self):
        """Test updating an exhibit"""
        data = {
            'title': 'Updated Title',
            'domain': 'Healthcare',
            'backgroundDeploymentContext': 'Updated context',
            'intededUse': 'Updated use',
            'viewNumber': 10
        }
        response = self.client.put(f'/api/exhibits/{self.exhibit1.exhibitId}/edit', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.exhibit1.refresh_from_db()
        self.assertEqual(self.exhibit1.title, 'Updated Title')
        
    def test_delete_exhibit_success(self):
        """Test deleting an exhibit"""
        response = self.client.delete(f'/api/exhibits/{self.exhibit1.exhibitId}/edit')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Exhibit.objects.count(), 1)


class ArtefactAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.artefact = Artefact.objects.create(
            info="Test artefact",
            artefactDate=date(2024, 1, 1),
            artefactObjectPath="/path/to/object",
            exhibitId=self.exhibit
        )
        
    def test_create_artefact_success(self):
        """Test creating a new artefact"""
        data = {
            'info': 'New artefact',
            'artefactDate': '2024-02-01',
            'artefactObjectPath': '/new/path'
        }
        response = self.client.post(f'/api/exhibits/{self.exhibit.exhibitId}/artefacts/new', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artefact.objects.count(), 2)
        
    def test_create_artefact_invalid_exhibit(self):
        """Test creating artefact with non-existent exhibit"""
        data = {
            'info': 'New artefact',
            'artefactDate': '2024-02-01',
            'artefactObjectPath': '/new/path'
        }
        response = self.client.post('/api/exhibits/9999/artefacts/new', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_get_artefact_success(self):
        """Test retrieving an artefact"""
        response = self.client.get(f'/api/exhibits/{self.exhibit.exhibitId}/artefacts/edit/{self.artefact.artefactId}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['info'], 'Test artefact')
        
    def test_update_artefact_success(self):
        """Test updating an artefact"""
        data = {
            'info': 'Updated artefact',
            'artefactDate': '2024-03-01',
            'artefactObjectPath': '/updated/path'
        }
        response = self.client.put(f'/api/exhibits/{self.exhibit.exhibitId}/artefacts/edit/{self.artefact.artefactId}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artefact.refresh_from_db()
        self.assertEqual(self.artefact.info, 'Updated artefact')
        
    def test_delete_artefact_success(self):
        """Test deleting an artefact"""
        response = self.client.delete(f'/api/exhibits/{self.exhibit.exhibitId}/artefacts/edit/{self.artefact.artefactId}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artefact.objects.count(), 0)


class SystemDescriptionAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        # Mock the isCurator permission to always return True for tests
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        
    def test_create_system_description_success(self):
        """Test creating a system description"""
        data = {
            'systemDescription': 'Test system',
            'systemPurpose': 'Test purpose',
            'systemOutputs': 'Test outputs'
        }
        response = self.client.post(f'/api/exhibits/{self.exhibit.exhibitId}/aiSystemDescription/new', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AiSystemDescription.objects.count(), 1)
        
    def test_get_system_description_success(self):
        """Test retrieving a system description"""
        system_desc = AiSystemDescription.objects.create(
            exhibitId=self.exhibit,  # Changed from exhibit= to exhibitId=
            systemDescription='Test',
            systemPurpose='Purpose',
            systemOutputs='Outputs'
        )
        response = self.client.get(f'/api/exhibits/{self.exhibit.exhibitId}/aiSystemDescription/edit/{system_desc.systemDescriptionId}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_system_description_success(self):
        """Test updating a system description"""
        system_desc = AiSystemDescription.objects.create(
            exhibitId=self.exhibit,  # Changed from exhibit= to exhibitId=
            systemDescription='Test',
            systemPurpose='Purpose',
            systemOutputs='Outputs'
        )
        data = {
            'systemDescription': 'Updated system',
            'systemPurpose': 'Updated purpose',
            'systemOutputs': 'Updated outputs'
        }
        response = self.client.put(f'/api/exhibits/{self.exhibit.exhibitId}/aiSystemDescription/edit/{system_desc.systemDescriptionId}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class FailureDescriptionAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        # Mock the isCurator permission to always return True for tests
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        
    def test_create_failure_description_success(self):
        """Test creating a failure description"""
        data = {
            'whatWentWrong': 'Something failed',
            'howItWasDetected': 'We noticed',
            'whatWasAffected': 'Users impacted'
        }
        response = self.client.post(f'/api/exhibits/{self.exhibit.exhibitId}/failureDescription/new', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_delete_failure_description_success(self):
        """Test deleting a failure description"""
        failure_desc = FailureDescription.objects.create(
            exhibit=self.exhibit,  # Changed from exhibit= to exhibitId=
            whatWentWrong='Test',
            howItWasDetected='Test',
            whatWasAffected='Test'
        )
        response = self.client.delete(f'/api/exhibits/{self.exhibit.exhibitId}/failureDescription/edit/{failure_desc.failureDescriptioniId}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LessonsLearnedAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        
    def test_create_lesson_learned_success(self):
        """Test creating a lesson learned"""
        data = {
            'practicalRecommendations': 'Do this better',
            'futureWarnings': 'Watch out for this'
        }
        response = self.client.post(f'/api/exhibits/{self.exhibit.exhibitId}/lessonsLearned/new', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_lesson_learned_success(self):
        """Test retrieving a lesson learned"""
        lesson = LessonsLearned.objects.create(
            exhibitId=self.exhibit,
            practicalRecommendations='Test',
            futureWarnings='Test'
        )
        response = self.client.get(f'/api/exhibits/{self.exhibit.exhibitId}/lessonsLearned/edit/{lesson.lessonslearnedId}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ContributingFactorsAPITestCase(APITestCase):
    
    def setUp(self):
        """Create test data before each test"""
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
        
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        
    def test_create_contributing_factor_success(self):
        """Test creating a contributing factor"""
        data = {
            'dataIssues': 'Bad data',
            'designChoices': 'Poor design',
            'organisationalOrGovernanceIssues': 'Lack of oversight'
        }
        response = self.client.post(f'/api/exhibits/{self.exhibit.exhibitId}/contributingFactors/new', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_contributing_factor_success(self):
        """Test updating a contributing factor"""
        factor = ContributingFactors.objects.create(
            exhibitId=self.exhibit,
            dataIssues='Test',
            designChoices='Test',
            organisationalOrGovernanceIssues='Test'
        )
        data = {
            'dataIssues': 'Updated data issues',
            'designChoices': 'Updated design',
            'organisationalOrGovernanceIssues': 'Updated governance'
        }
        response = self.client.put(f'/api/exhibits/{self.exhibit.exhibitId}/contributingFactors/edit/{factor.contributingFactorId}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthenticationTestCase(APITestCase):
    
    def setUp(self):
        """Create test user and exhibit"""
        # Create Curator group
        curator_group, created = Group.objects.get_or_create(name='Curator')
        
        # Create curator user
        self.curator_user = User.objects.create_user(username='curator', password='testpass123')
        self.curator_user.groups.add(curator_group)
        
        # Create non-curator user
        self.regular_user = User.objects.create_user(username='regularuser', password='testpass123')
        
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
    
    def test_unauthenticated_get_fails(self):
        """Test that unauthenticated GET requests are rejected"""
        response = self.client.get('/api/exhibits/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_unauthenticated_post_fails(self):
        """Test that unauthenticated POST requests are rejected"""
        data = {
            'title': 'New Exhibit',
            'domain': 'Finance',
            'backgroundDeploymentContext': 'Context',
            'intededUse': 'Use',
            'viewNumber': 0
        }
        response = self.client.post('/api/exhibits/viewCreate', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_authenticated_curator_get_succeeds(self):
        """Test that authenticated curator GET requests succeed"""
        self.client.force_authenticate(user=self.curator_user)
        response = self.client.get('/api/exhibits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_authenticated_curator_post_succeeds(self):
        """Test that authenticated curator POST requests succeed"""
        self.client.force_authenticate(user=self.curator_user)
        data = {
            'title': 'New Exhibit',
            'domain': 'Finance',
            'backgroundDeploymentContext': 'Context',
            'intededUse': 'Use',
            'viewNumber': 0
        }
        response = self.client.post('/api/exhibits/viewCreate', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_non_curator_user_denied(self):
        """Test that authenticated non-curator users are denied"""
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'title': 'New Exhibit',
            'domain': 'Finance',
            'backgroundDeploymentContext': 'Context',
            'intededUse': 'Use',
            'viewNumber': 0
        }
        response = self.client.post('/api/exhibits/viewCreate', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_logout_prevents_access(self):
        """Test that logging out prevents access"""
        self.client.force_authenticate(user=self.curator_user)
        response = self.client.get('/api/exhibits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Logout
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/exhibits/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
